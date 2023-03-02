from views import chose_form_view
from PyQt5 import QtWidgets ,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
from PyQt5 import QtCore, QtMultimedia
import cv2
import os
import multiprocessing
import time





class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    alert_sound = pyqtSignal()
    def __init__(self , *args , **kwargs):
        super().__init__()
        
        cv2_base_dir = os.path.dirname(cv2.__file__)
        target_face_classfier = os.path.join(cv2_base_dir , "data" , "haarcascade_frontalface_default.xml")#categrized
        target_eye_calssfier  = os.path.join(cv2_base_dir , "data" , "haarcascade_eye_tree_eyeglasses.xml")
        self.faceCascade = cv2.CascadeClassifier(target_face_classfier)
        self.eyeCascade = cv2.CascadeClassifier(target_eye_calssfier)

        self.run_sound = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        cap.set(3 , 1360)
        cap.set(4 , 768)
        while True:
            ret, img = cap.read() #ret camera mode & img img frame
            if ret:
                img = cv2.flip(img, 1)
                try :
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = self.faceCascade.detectMultiScale(
                        gray,
                        scaleFactor=1.1, # image scale
                        minNeighbors=15,
                        minSize=(30, 30),
                    )

                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        roi_face = gray[y:y + h, x:x + w]
                        roi_face_clr = img[y:y + h, x:x + w]
                        eyes = self.eyeCascade.detectMultiScale(roi_face, 1.3, 5, minSize=(50, 50))

                        if len(eyes) >= 2 :
                            print("eyes opened")
                        elif len(eyes) ==1 :
                            print("one eye opened")
                        else:
                            if self.run_sound :
                                self.alert_sound.emit()
                                self.run_sound = False
                                print("signal sent")
                            print("eyes closed")
                except Exception as e :
                    print(e)
                self.change_pixmap_signal.emit(img)



class Chose_form_manger(QtWidgets.QWidget, chose_form_view.Ui_Form):
    def __init__(self):
        super(Chose_form_manger, self).__init__()
        self.setupUi(self)

        self.disply_width = 1280
        self.display_height = 720

        try :
            # create the video capture thread
            self.thread = VideoThread()
            # connect its signal to the update_image slot
            self.thread.change_pixmap_signal.connect(self.update_image)
            # start the thread
            # self.thread.start()

            self.thread.alert_sound.connect(self.run_sound)
        except Exception as e :
            print(e)
        self.player = QtMultimedia.QMediaPlayer()

    def run_sound(self):
        try :
            url = QtCore.QUrl.fromLocalFile('alert.mp3')
            self.player.setMedia(QtMultimedia.QMediaContent(url))

            self.player.play()
        except Exception as e :
            print(e)


    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        try :
            """Updates the image_label with a new opencv image"""
            qt_img = self.convert_cv_qt(cv_img)
            self.camera_lbl.setPixmap(qt_img)
        except Exception as r :
            print(r)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    window = Chose_form_manger()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
