# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContourDiff_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import UIController
from CanvasClass import Canvas
from DistrbutionCanvas import DistrbutionCanvas
import DataProcessing
import GenerateImages
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1249, 884)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Whole_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Whole_Frame.setGeometry(QtCore.QRect(10, 10, 1231, 831))
        self.Whole_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Whole_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Whole_Frame.setObjectName("Whole_Frame")
        self.label_Control = QtWidgets.QLabel(self.Whole_Frame)
        self.label_Control.setGeometry(QtCore.QRect(1040, 0, 161, 21))


        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)

        self.filenameToPathDict = {}
        #Space for plotting the image
        self.label_Control.setFont(font)
        self.label_Control.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_Control.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Control.setObjectName("label_Control")

        # self.graphicsView_Image = QtWidgets.QGraphicsView(self.Whole_Frame)
        # self.graphicsView_Image.setGeometry(QtCore.QRect(0, 0, 1011, 781))
        # self.draw_image()




        font = QtGui.QFont()
        font.setPointSize(11)
        line_edit_font = QtGui.QFont()
        line_edit_font.setPointSize(7)
        line_edit_font.setBold(False)
        line_edit_font.setWeight(50)
        self.layoutWidget = QtWidgets.QWidget(self.Whole_Frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 800, 1222, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_value = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_value.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_value.setObjectName("horizontalLayout_value")
        self.label_X = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_X.setFont(font)
        self.label_X.setObjectName("label_X")
        self.horizontalLayout_value.addWidget(self.label_X)
        self.line_X = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_X.setObjectName("line_X")
        self.horizontalLayout_value.addWidget(self.line_X)
        self.label_Y = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Y.setFont(font)
        self.label_Y.setObjectName("label_Y")
        self.horizontalLayout_value.addWidget(self.label_Y)
        self.line_Y = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_Y.setObjectName("line_Y")
        self.horizontalLayout_value.addWidget(self.line_Y)
        self.label_value = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_value.setFont(font)
        self.label_value.setObjectName("label_value")
        self.horizontalLayout_value.addWidget(self.label_value)
        self.line_Value = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_Value.setObjectName("line_Value")
        self.horizontalLayout_value.addWidget(self.line_Value)
        self.control_frame = QtWidgets.QFrame(self.Whole_Frame)
        self.control_frame.setGeometry(QtCore.QRect(1010, 20, 211, 761))
        self.control_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control_frame.setObjectName("control_frame")
        self.groupBox_map_properties = QtWidgets.QGroupBox(self.control_frame)
        self.groupBox_map_properties.setGeometry(QtCore.QRect(10, 325, 191, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_map_properties.setFont(font)
        self.groupBox_map_properties.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_map_properties.setObjectName("groupBox_map_properties")
        self.label_Quadtree = QtWidgets.QLabel(self.groupBox_map_properties)
        self.label_Quadtree.setGeometry(QtCore.QRect(1, 22, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

        #comboboxfont
        comboboxfont = QtGui.QFont()
        comboboxfont.setPointSize(8)
        comboboxfont.setBold(False)
        comboboxfont.setWeight(50)




        self.label_Quadtree.setFont(font)
        self.label_Quadtree.setObjectName("label_Quadtree")
        self.label_Direction = QtWidgets.QLabel(self.groupBox_map_properties)
        self.label_Direction.setGeometry(QtCore.QRect(-2, 53, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_Direction.setFont(font)
        self.label_Direction.setObjectName("label_Direction")
        self.comboBox_Quadtree = QtWidgets.QComboBox(self.groupBox_map_properties)
        self.comboBox_Quadtree.setFont(comboboxfont)
        self.comboBox_Quadtree.setGeometry(QtCore.QRect(89, 21, 101, 18))
        self.comboBox_Quadtree.setFrame(True)
        self.comboBox_Quadtree.setObjectName("comboBox_Quadtree")
        self.setCombox_Quadtree()


        self.label_content = QtWidgets.QLabel(self.groupBox_map_properties)
        self.label_content.setGeometry(QtCore.QRect(1, 83, 70, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_content.setFont(font)
        self.label_content.setObjectName("label_content")
        self.checkBox_content_contours = QtWidgets.QCheckBox(self.groupBox_map_properties)
        self.checkBox_content_contours.setGeometry(QtCore.QRect(60, 83, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_content_contours.setFont(font)
        self.checkBox_content_contours.setObjectName("checkBox_content_contours")
        self.checkBox_content_vectors = QtWidgets.QCheckBox(self.groupBox_map_properties)
        self.checkBox_content_vectors.setGeometry(QtCore.QRect(130, 83, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_content_vectors.setFont(font)
        self.checkBox_content_vectors.setObjectName("checkBox_content_vectors")
        self.checkBox_direction_positive = QtWidgets.QCheckBox(self.groupBox_map_properties)
        self.checkBox_direction_positive.setGeometry(QtCore.QRect(60, 53, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_direction_positive.setFont(font)
        self.checkBox_direction_positive.setObjectName("checkBox_direction_positive")
        self.checkBox_direction_negative = QtWidgets.QCheckBox(self.groupBox_map_properties)
        self.checkBox_direction_negative.setGeometry(QtCore.QRect(130, 53, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_direction_negative.setFont(font)
        self.checkBox_direction_negative.setObjectName("checkBox_direction_negative")
        self.label_magnitude = QtWidgets.QLabel(self.groupBox_map_properties)
        self.label_magnitude.setGeometry(QtCore.QRect(0, 110, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_magnitude.setFont(font)
        self.label_magnitude.setObjectName("label_magnitude")
        self.frame_magnitude = QtWidgets.QFrame(self.groupBox_map_properties)
        self.frame_magnitude.setGeometry(QtCore.QRect(60, 110, 130, 18))
        self.frame_magnitude.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_magnitude.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_magnitude.setObjectName("frame_magnitude")
        self.horizontalSlider_magnitude = QtWidgets.QSlider(self.frame_magnitude)
        self.horizontalSlider_magnitude.setGeometry(QtCore.QRect(2, 0, 95, 18))
        self.horizontalSlider_magnitude.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_magnitude.setObjectName("horizontalSlider_magnitude")
        # self.setHorizontalMagnitude()
        self.lineEdit_magnitude = QtWidgets.QLineEdit(self.frame_magnitude)
        self.lineEdit_magnitude.setFont(line_edit_font)
        self.lineEdit_magnitude.setGeometry(QtCore.QRect(99, 0, 30, 17))
        self.lineEdit_magnitude.setObjectName("lineEdit_magnitude")
        self.pushButton_mapproperties_apply = QtWidgets.QPushButton(self.groupBox_map_properties)
        self.pushButton_mapproperties_apply.setGeometry(QtCore.QRect(99, 134, 93, 21))
        self.setHorizontalMagnitude()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mapproperties_apply.setFont(font)
        self.pushButton_mapproperties_apply.setObjectName("pushButton_mapproperties_apply")
        self.pushButton_mapproperties_reset = QtWidgets.QPushButton(self.groupBox_map_properties)
        self.pushButton_mapproperties_reset.setGeometry(QtCore.QRect(0, 134, 93, 21))
        #Listener for apply in Map Properties
        self.pushButton_mapproperties_apply.clicked.connect(self.pushButton_mapproperties_apply_listener)
        #Listener for reset in Map Properties
        self.pushButton_mapproperties_reset.clicked.connect(self.pushButton_mapproperties_reset_listener)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mapproperties_reset.setFont(font)
        self.pushButton_mapproperties_reset.setObjectName("pushButton_mapproperties_reset")
        self.groupBox_data_properties = QtWidgets.QGroupBox(self.control_frame)
        self.groupBox_data_properties.setGeometry(QtCore.QRect(10, 69, 191, 252))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_data_properties.setFont(font)
        self.groupBox_data_properties.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_data_properties.setObjectName("groupBox_data_properties")
        self.label_isoline1 = QtWidgets.QLabel(self.groupBox_data_properties)
        self.label_isoline1.setGeometry(QtCore.QRect(0, 157, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_isoline1.setFont(font)
        self.label_isoline1.setObjectName("label_isoline1")
        self.label_isoline2 = QtWidgets.QLabel(self.groupBox_data_properties)
        self.label_isoline2.setGeometry(QtCore.QRect(0, 180, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_isoline2.setFont(font)
        self.label_isoline2.setObjectName("label_isoline2")
        self.label_isoline3 = QtWidgets.QLabel(self.groupBox_data_properties)
        self.label_isoline3.setGeometry(QtCore.QRect(0, 202, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_isoline3.setFont(font)
        self.label_isoline3.setObjectName("label_isoline3")
        self.pushButton_distribution = QtWidgets.QPushButton(self.groupBox_data_properties)
        self.pushButton_distribution.setGeometry(QtCore.QRect(0, 16, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_distribution.setFont(font)
        self.pushButton_distribution.setObjectName("pushButton_distribution")
        self.pushButton_distribution.clicked.connect(self.setPushButton_distrbution)


        # DistrbutionCanvas
        # self.graphicsView_distribution = QtWidgets.QGraphicsView(self.groupBox_data_properties)
        # self.graphicsView_distribution.setGeometry(QtCore.QRect(0, 40, 191, 101))
        # self.graphicsView_distribution.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.graphicsView_distribution.setObjectName("graphicsView_distribution")


        self.dist_canvas = DistrbutionCanvas(self.groupBox_data_properties)
        self.dist_canvas.setGeometry(QtCore.QRect(0, 40, 191, 101))




        #UI group to set levels

        self.frame_isoline1 = QtWidgets.QFrame(self.groupBox_data_properties)
        self.frame_isoline1.setGeometry(QtCore.QRect(50, 155, 140, 21))
        self.frame_isoline1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_isoline1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_isoline1.setObjectName("frame_isoline1")
        self.horizontalSlider_isoline1 = QtWidgets.QSlider(self.frame_isoline1)
        self.horizontalSlider_isoline1.setGeometry(QtCore.QRect(3, 0, 103, 21))
        self.horizontalSlider_isoline1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_isoline1.setObjectName("horizontalSlider_isoline1")
        self.lineEdit_isoline1 = QtWidgets.QLineEdit(self.frame_isoline1)
        self.lineEdit_isoline1.setGeometry(QtCore.QRect(109, 0, 30, 20))
        self.lineEdit_isoline1.setObjectName("lineEdit_isoline1")
        self.lineEdit_isoline1.setFont(line_edit_font)

        #set horizontal slider 1
        self.setIsoLineSlider1()

        self.frame_isoline2 = QtWidgets.QFrame(self.groupBox_data_properties)
        self.frame_isoline2.setGeometry(QtCore.QRect(50, 178, 140, 21))
        self.frame_isoline2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_isoline2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_isoline2.setObjectName("frame_isoline2")

        self.horizontalSlider_isoline2 = QtWidgets.QSlider(self.frame_isoline2)
        self.horizontalSlider_isoline2.setGeometry(QtCore.QRect(3, 0, 103, 21))
        self.horizontalSlider_isoline2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_isoline2.setObjectName("horizontalSlider_isoline2")

        self.lineEdit_isoline2 = QtWidgets.QLineEdit(self.frame_isoline2)
        self.lineEdit_isoline2.setGeometry(QtCore.QRect(109, 0, 30, 20))
        self.lineEdit_isoline2.setObjectName("lineEdit_isoline2")
        self.lineEdit_isoline2.setFont(line_edit_font)
        self.setIsoLineSlider2()

        self.frame_isoline3 = QtWidgets.QFrame(self.groupBox_data_properties)
        self.frame_isoline3.setGeometry(QtCore.QRect(50, 201, 140, 21))
        self.frame_isoline3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_isoline3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_isoline3.setObjectName("frame_isoline3")

        self.horizontalSlider_isoline3 = QtWidgets.QSlider(self.frame_isoline3)
        self.horizontalSlider_isoline3.setGeometry(QtCore.QRect(3, 0, 103, 21))
        self.horizontalSlider_isoline3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_isoline3.setObjectName("horizontalSlider_isoline3")
        self.lineEdit_isoline3 = QtWidgets.QLineEdit(self.frame_isoline3)
        self.lineEdit_isoline3.setGeometry(QtCore.QRect(109, 0, 30, 20))
        self.lineEdit_isoline3.setObjectName("lineEdit_isoline3")
        self.lineEdit_isoline3.setFont(line_edit_font)
        self.setIsoLineSlider3()

        self.pushButton_dataproperties_reset = QtWidgets.QPushButton(self.groupBox_data_properties)
        self.pushButton_dataproperties_reset.setGeometry(QtCore.QRect(0, 227, 93, 21))


        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_dataproperties_reset.setFont(font)
        self.pushButton_dataproperties_reset.setObjectName("pushButton_dataproperties_reset")
        self.pushButton_dataproperties_apply = QtWidgets.QPushButton(self.groupBox_data_properties)
        self.pushButton_dataproperties_apply.setGeometry(QtCore.QRect(99, 227, 93, 21))
        #Listener data properties reset
        self.pushButton_dataproperties_reset.clicked.connect(self.pushButton_dataproperties_reset_listener)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_dataproperties_apply.setFont(font)
        self.pushButton_dataproperties_apply.setObjectName("pushButton_dataproperties_apply")
        # Listener data properties reset
        self.pushButton_dataproperties_apply.clicked.connect(self.pushButton_dataproperties_apply_listener)
        self.groupBox_datadirectory = QtWidgets.QGroupBox(self.control_frame)
        self.groupBox_datadirectory.setGeometry(QtCore.QRect(10, 3, 191, 65))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_datadirectory.setFont(font)
        self.groupBox_datadirectory.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_datadirectory.setObjectName("groupBox_datadirectory")
        self.pushButton_obs_dir = QtWidgets.QPushButton(self.groupBox_datadirectory)
        self.pushButton_obs_dir.setGeometry(QtCore.QRect(150, 42, 41, 18))
        self.pushButton_obs_dir.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_obs_dir.setIcon(icon)
        self.pushButton_obs_dir.setObjectName("pushButton_obs_dir")
        self.label_obs_dir = QtWidgets.QLabel(self.groupBox_datadirectory)
        self.label_obs_dir.setGeometry(QtCore.QRect(0, 42, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_obs_dir.setFont(font)
        self.label_obs_dir.setFrameShape(QtWidgets.QFrame.Box)
        self.label_obs_dir.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_obs_dir.setLineWidth(1)
        self.label_obs_dir.setMidLineWidth(0)
        self.label_obs_dir.setObjectName("label_obs_dir")
        self.label_currentfile = QtWidgets.QLabel(self.groupBox_datadirectory)
        self.label_currentfile.setGeometry(QtCore.QRect(0, 20, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_currentfile.setFont(font)
        self.label_currentfile.setFrameShape(QtWidgets.QFrame.Box)
        self.label_currentfile.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_currentfile.setLineWidth(1)
        self.label_currentfile.setMidLineWidth(0)
        self.label_currentfile.setObjectName("label_currentfile")
        self.pushButton_currentfile = QtWidgets.QPushButton(self.groupBox_datadirectory)
        self.pushButton_currentfile.setGeometry(QtCore.QRect(150, 20, 41, 18))
        self.pushButton_currentfile.setText("")
        self.pushButton_currentfile.setIcon(icon)
        self.pushButton_currentfile.setObjectName("pushButton_currentfile")
        self.groupBox_content_properties = QtWidgets.QGroupBox(self.control_frame)
        self.groupBox_content_properties.setGeometry(QtCore.QRect(10, 490, 191, 275))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_content_properties.setFont(font)
        self.groupBox_content_properties.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_content_properties.setObjectName("groupBox_content_properties")
        self.tabWidget_content_properties = QtWidgets.QTabWidget(self.groupBox_content_properties)
        self.tabWidget_content_properties.setGeometry(QtCore.QRect(0, 20, 191, 253))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_content_properties.setFont(font)
        self.tabWidget_content_properties.setAutoFillBackground(False)
        self.tabWidget_content_properties.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_content_properties.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_content_properties.setObjectName("tabWidget_content_properties")
        self.Contour = QtWidgets.QWidget()
        self.Contour.setObjectName("Contour")
        self.groupBox_contours = QtWidgets.QGroupBox(self.Contour)
        self.groupBox_contours.setGeometry(QtCore.QRect(-1, 9, 188, 97))
        self.groupBox_contours.setAutoFillBackground(False)
        self.groupBox_contours.setFlat(False)
        self.groupBox_contours.setCheckable(True)
        self.groupBox_contours.setObjectName("groupBox_contours")
        self.checkBox_fill_contours = QtWidgets.QCheckBox(self.groupBox_contours)
        self.checkBox_fill_contours.setGeometry(QtCore.QRect(150, 20, 37, 17))
        self.checkBox_fill_contours.setObjectName("checkBox_fill_contours")
        self.label_colormap_contours = QtWidgets.QLabel(self.groupBox_contours)
        self.label_colormap_contours.setGeometry(QtCore.QRect(1, 45, 47, 13))
        self.label_colormap_contours.setObjectName("label_colormap_contours")
        self.frame_opacity_contours = QtWidgets.QFrame(self.groupBox_contours)
        self.frame_opacity_contours.setGeometry(QtCore.QRect(50, 70, 136, 21))
        self.frame_opacity_contours.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_opacity_contours.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_opacity_contours.setObjectName("frame_opacity_contours")
        self.horizontalSlider_opacity_contours = QtWidgets.QSlider(self.frame_opacity_contours)
        self.horizontalSlider_opacity_contours.setGeometry(QtCore.QRect(3, 0, 103, 21))
        self.horizontalSlider_opacity_contours.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_opacity_contours.setObjectName("horizontalSlider_opacity_contours")
        self.lineEdit_opacity_contours = QtWidgets.QLineEdit(self.frame_opacity_contours)
        self.lineEdit_opacity_contours.setGeometry(QtCore.QRect(108, 0, 27, 20))
        self.lineEdit_opacity_contours.setObjectName("lineEdit_opacity_contours")
        self.label_opacity_contours = QtWidgets.QLabel(self.groupBox_contours)
        self.label_opacity_contours.setGeometry(QtCore.QRect(1, 70, 47, 13))
        self.label_opacity_contours.setObjectName("label_opacity_contours")
        self.label_fill_contours = QtWidgets.QLabel(self.groupBox_contours)
        self.label_fill_contours.setGeometry(QtCore.QRect(1, 20, 71, 16))
        self.label_fill_contours.setObjectName("label_fill_contours")
        self.comboBox_colormap_contours = QtWidgets.QComboBox(self.groupBox_contours)
        self.comboBox_colormap_contours.setGeometry(QtCore.QRect(52, 42, 134, 22))
        self.comboBox_colormap_contours.setIconSize(QtCore.QSize(75, 40))
        self.comboBox_colormap_contours.setObjectName("comboBox_colormap_contours")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/obspy-imaging-cm-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_colormap_contours.addItem(icon1, "")
        self.groupBox_lines = QtWidgets.QGroupBox(self.Contour)
        self.groupBox_lines.setGeometry(QtCore.QRect(-1, 116, 188, 111))
        self.groupBox_lines.setCheckable(True)
        self.groupBox_lines.setObjectName("groupBox_lines")
        self.frame_opacity_lines = QtWidgets.QFrame(self.groupBox_lines)
        self.frame_opacity_lines.setGeometry(QtCore.QRect(52, 50, 134, 21))
        self.frame_opacity_lines.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_opacity_lines.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_opacity_lines.setObjectName("frame_opacity_lines")
        self.horizontalSlider_opacity_lines = QtWidgets.QSlider(self.frame_opacity_lines)
        self.horizontalSlider_opacity_lines.setGeometry(QtCore.QRect(3, 0, 102, 21))
        self.horizontalSlider_opacity_lines.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_opacity_lines.setObjectName("horizontalSlider_opacity_lines")
        self.lineEdit_opacity_lines = QtWidgets.QLineEdit(self.frame_opacity_lines)
        self.lineEdit_opacity_lines.setGeometry(QtCore.QRect(106, 0, 27, 20))
        self.lineEdit_opacity_lines.setObjectName("lineEdit_opacity_lines")
        self.label_color_lines = QtWidgets.QLabel(self.groupBox_lines)
        self.label_color_lines.setGeometry(QtCore.QRect(1, 25, 47, 13))
        self.label_color_lines.setObjectName("label_color_lines")
        self.label_opacity = QtWidgets.QLabel(self.groupBox_lines)
        self.label_opacity.setGeometry(QtCore.QRect(1, 52, 47, 13))
        self.label_opacity.setObjectName("label_opacity")
        self.comboBox_color_lines = QtWidgets.QComboBox(self.groupBox_lines)
        self.comboBox_color_lines.setGeometry(QtCore.QRect(53, 22, 133, 22))
        self.comboBox_color_lines.setIconSize(QtCore.QSize(75, 40))
        self.comboBox_color_lines.setObjectName("comboBox_color_lines")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/index.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_color_lines.addItem(icon2, "")
        self.frame_line_width = QtWidgets.QFrame(self.groupBox_lines)
        self.frame_line_width.setGeometry(QtCore.QRect(52, 77, 134, 21))
        self.frame_line_width.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_line_width.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_line_width.setObjectName("frame_line_width")
        self.horizontalSlider_line_width = QtWidgets.QSlider(self.frame_line_width)
        self.horizontalSlider_line_width.setGeometry(QtCore.QRect(3, 0, 102, 21))
        self.horizontalSlider_line_width.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_line_width.setObjectName("horizontalSlider_line_width")
        self.lineEdit_line_width = QtWidgets.QLineEdit(self.frame_line_width)
        self.lineEdit_line_width.setGeometry(QtCore.QRect(106, 0, 27, 20))
        self.lineEdit_line_width.setObjectName("lineEdit_line_width")
        self.label_line_width = QtWidgets.QLabel(self.groupBox_lines)
        self.label_line_width.setGeometry(QtCore.QRect(1, 78, 51, 16))
        self.label_line_width.setObjectName("label_line_width")
        self.tabWidget_content_properties.addTab(self.Contour, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_arrow = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_arrow.setGeometry(QtCore.QRect(-1, 10, 188, 111))
        self.groupBox_arrow.setCheckable(True)
        self.groupBox_arrow.setObjectName("groupBox_arrow")
        self.frame_arrow_width = QtWidgets.QFrame(self.groupBox_arrow)
        self.frame_arrow_width.setGeometry(QtCore.QRect(69, 50, 117, 21))
        self.frame_arrow_width.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_arrow_width.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_arrow_width.setObjectName("frame_arrow_width")
        self.horizontalSlider_arrow_width = QtWidgets.QSlider(self.frame_arrow_width)
        self.horizontalSlider_arrow_width.setGeometry(QtCore.QRect(3, 0, 85, 21))
        self.horizontalSlider_arrow_width.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_arrow_width.setObjectName("horizontalSlider_arrow_width")
        self.lineEdit_arrow_width = QtWidgets.QLineEdit(self.frame_arrow_width)
        self.lineEdit_arrow_width.setGeometry(QtCore.QRect(90, 0, 26, 20))
        self.lineEdit_arrow_width.setObjectName("lineEdit_arrow_width")
        self.frame_arrow_length = QtWidgets.QFrame(self.groupBox_arrow)
        self.frame_arrow_length.setGeometry(QtCore.QRect(69, 19, 117, 21))
        self.frame_arrow_length.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_arrow_length.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_arrow_length.setObjectName("frame_arrow_length")
        self.horizontalSlider_arrow_length = QtWidgets.QSlider(self.frame_arrow_length)
        self.horizontalSlider_arrow_length.setGeometry(QtCore.QRect(3, 0, 85, 21))
        self.horizontalSlider_arrow_length.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_arrow_length.setObjectName("horizontalSlider_arrow_length")
        self.lineEdit_arrow_length = QtWidgets.QLineEdit(self.frame_arrow_length)
        self.lineEdit_arrow_length.setGeometry(QtCore.QRect(90, 0, 26, 20))
        self.lineEdit_arrow_length.setObjectName("lineEdit_arrow_length")
        self.label_arrow_width = QtWidgets.QLabel(self.groupBox_arrow)
        self.label_arrow_width.setGeometry(QtCore.QRect(1, 50, 68, 16))
        self.label_arrow_width.setObjectName("label_arrow_width")
        self.label_arrow_length = QtWidgets.QLabel(self.groupBox_arrow)
        self.label_arrow_length.setGeometry(QtCore.QRect(1, 20, 68, 16))
        self.label_arrow_length.setObjectName("label_arrow_length")
        self.label_arrow_color = QtWidgets.QLabel(self.groupBox_arrow)
        self.label_arrow_color.setGeometry(QtCore.QRect(1, 82, 47, 13))
        self.label_arrow_color.setObjectName("label_arrow_color")
        self.comboBox_arrow_color = QtWidgets.QComboBox(self.groupBox_arrow)
        self.comboBox_arrow_color.setGeometry(QtCore.QRect(45, 80, 141, 20))
        self.comboBox_arrow_color.setIconSize(QtCore.QSize(75, 40))
        self.comboBox_arrow_color.setObjectName("comboBox_arrow_color")
        self.comboBox_arrow_color.addItem(icon2, "")
        self.tabWidget_content_properties.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1249, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.menuHome.setFont(font)
        self.menuHome.setObjectName("menuHome")
        self.menuGo_to = QtWidgets.QMenu(self.menubar)
        # self.menuGo_to.setObjectName("menuGo_to")
        # self.menuScaling = QtWidgets.QMenu(self.menubar)
        # self.menuScaling.setObjectName("menuScaling")
        # self.menuZooming = QtWidgets.QMenu(self.menubar)
        # self.menuZooming.setObjectName("menuZooming")
        # self.menuSave_Image = QtWidgets.QMenu(self.menubar)
        # self.menuSave_Image.setObjectName("menuSave_Image")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionForward = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon3)
        self.actionForward.setObjectName("actionForward")
        self.actionBackward = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBackward.setIcon(icon4)
        self.actionBackward.setObjectName("actionBackward")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.fileDialog)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/save-file-option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon6)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon7)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/download-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_2.setIcon(icon8)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_content_properties.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkBox_fill_contours.stateChanged.connect(self.setCheckBoxFillContours)


        self.canvas = Canvas(self.Whole_Frame, 10, 8, 100)
        self.checkBox_content_vectors.setChecked(True)
        self.checkBox_content_contours.setChecked(True)
        self.checkBox_direction_negative.setChecked(True)
        self.checkBox_direction_positive.setChecked(True)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Control.setText(_translate("MainWindow", "Control Panel"))
        self.label_X.setText(_translate("MainWindow", "X:"))
        self.label_Y.setText(_translate("MainWindow", "Y:"))
        self.label_value.setText(_translate("MainWindow", "Value: "))
        self.groupBox_map_properties.setTitle(_translate("MainWindow", "Map Properties"))
        self.label_Quadtree.setText(_translate("MainWindow", "Quadtree Depth"))
        self.label_Direction.setText(_translate("MainWindow", " Direction"))
        self.label_content.setText(_translate("MainWindow", "Content"))
        self.checkBox_content_contours.setText(_translate("MainWindow", "Contours"))
        self.checkBox_content_vectors.setText(_translate("MainWindow", "Vectors"))
        self.checkBox_direction_positive.setText(_translate("MainWindow", "Positive"))
        self.checkBox_direction_negative.setText(_translate("MainWindow", "Negative"))
        self.label_magnitude.setText(_translate("MainWindow", "Magnitude"))
        self.pushButton_mapproperties_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_mapproperties_reset.setText(_translate("MainWindow", "Reset"))
        self.groupBox_data_properties.setTitle(_translate("MainWindow", "Data Properties"))
        self.label_isoline1.setText(_translate("MainWindow", "Isoline 1"))
        self.label_isoline2.setText(_translate("MainWindow", "Isoline 2"))
        self.label_isoline3.setText(_translate("MainWindow", "Isoline 3"))
        self.pushButton_distribution.setText(_translate("MainWindow", "Distribution"))
        self.pushButton_dataproperties_reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_dataproperties_apply.setText(_translate("MainWindow", "Apply"))
        self.groupBox_datadirectory.setTitle(_translate("MainWindow", "Data Directory"))
        self.label_obs_dir.setText(_translate("MainWindow", "observations directory"))
        self.label_currentfile.setText(_translate("MainWindow", "current file"))
        self.groupBox_content_properties.setTitle(_translate("MainWindow", "Content Properties"))
        self.groupBox_contours.setTitle(_translate("MainWindow", "Contours"))
        self.checkBox_fill_contours.setText(_translate("MainWindow", "Yes"))
        self.label_colormap_contours.setText(_translate("MainWindow", "Colormap"))
        self.label_opacity_contours.setText(_translate("MainWindow", "Opacity"))
        self.label_fill_contours.setText(_translate("MainWindow", "Fill Contours"))
        self.comboBox_colormap_contours.setCurrentText(_translate("MainWindow", "Viridis"))
        self.comboBox_colormap_contours.setItemText(0, _translate("MainWindow", "Viridis"))
        self.groupBox_lines.setTitle(_translate("MainWindow", "Lines"))
        self.label_color_lines.setText(_translate("MainWindow", "Color"))
        self.label_opacity.setText(_translate("MainWindow", "Opacity"))
        self.comboBox_color_lines.setCurrentText(_translate("MainWindow", "Black"))
        self.comboBox_color_lines.setItemText(0, _translate("MainWindow", "Black"))
        self.label_line_width.setText(_translate("MainWindow", "Line Width"))
        self.tabWidget_content_properties.setTabText(self.tabWidget_content_properties.indexOf(self.Contour), _translate("MainWindow", "Contours"))
        self.groupBox_arrow.setTitle(_translate("MainWindow", "Arrow"))
        self.label_arrow_width.setText(_translate("MainWindow", "Arrow Width"))
        self.label_arrow_length.setText(_translate("MainWindow", "Arrow Length"))
        self.label_arrow_color.setText(_translate("MainWindow", "Color"))
        self.comboBox_arrow_color.setCurrentText(_translate("MainWindow", "Black"))
        self.comboBox_arrow_color.setItemText(0, _translate("MainWindow", "Black"))
        self.tabWidget_content_properties.setTabText(self.tabWidget_content_properties.indexOf(self.tab_2), _translate("MainWindow", "Vector"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        # self.menuHome.setTitle(_translate("MainWindow", "Home"))
        # self.menuGo_to.setTitle(_translate("MainWindow", "Go to"))
        # self.menuScaling.setTitle(_translate("MainWindow", "Scaling"))
        # self.menuZooming.setTitle(_translate("MainWindow", "Zooming"))
        # self.menuSave_Image.setTitle(_translate("MainWindow", "Save Image"))
        self.actionForward.setText(_translate("MainWindow", "Forward"))
        self.actionBackward.setText(_translate("MainWindow", "Backward"))
        # self.actionNew.setText(_translate("MainWindow", "New"))
        # self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+o"))
        self.actionSave.setText(_translate("MainWindow", "Save File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+s"))
        # self.actionClose.setText(_translate("MainWindow", "Close File "))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+q"))
        # self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        # self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        # self.actionSave_2.setText(_translate("MainWindow", "Save"))
        # self.actionSave_as.setText(_translate("MainWindow", "Save as..."))

    """"""
    def setIsoLineSlider1(self):
        self.horizontalSlider_isoline1.setMinimum(0)
        self.horizontalSlider_isoline1.setMaximum(100)
        self.horizontalSlider_isoline1.setTickInterval(1)
        self.horizontalSlider_isoline1.setValue(25)
        self.lineEdit_isoline1.setText(str(self.horizontalSlider_isoline1.value() / 100))
        self.horizontalSlider_isoline1.valueChanged.connect(self.setIsoLineSlider1Listener)
    def setIsoLineSlider1Listener(self):
        value = self.horizontalSlider_isoline1.value() / 100
        self.lineEdit_isoline1.setText(str(value))
        return self.lineEdit_isoline1

    def setIsoLineSlider2(self):
        self.horizontalSlider_isoline2.setMinimum(0)
        self.horizontalSlider_isoline2.setMaximum(100)
        self.horizontalSlider_isoline2.setTickInterval(1)
        self.horizontalSlider_isoline2.setValue(50)
        self.lineEdit_isoline2.setText(str(self.horizontalSlider_isoline2.value() / 100))
        self.horizontalSlider_isoline2.valueChanged.connect(self.setIsoLineSlider2Listener)

    def setIsoLineSlider2Listener(self):
        value = self.horizontalSlider_isoline2.value() / 100
        self.lineEdit_isoline2.setText(str(value))

    def setIsoLineSlider3(self):
        self.horizontalSlider_isoline3.setMinimum(0)
        self.horizontalSlider_isoline3.setMaximum(100)
        self.horizontalSlider_isoline3.setTickInterval(1)
        self.horizontalSlider_isoline3.setValue(75)
        self.lineEdit_isoline3.setText(str(self.horizontalSlider_isoline3.value() / 100))
        self.horizontalSlider_isoline3.valueChanged.connect(self.setIsoLineSlider3Listener)

    def setIsoLineSlider3Listener(self):
        value = self.horizontalSlider_isoline3.value() / 100
        self.lineEdit_isoline3.setText(str(value))

    def pushButton_dataproperties_reset_listener(self):
        self.setIsoLineSlider1()
        self.setIsoLineSlider2()
        self.setIsoLineSlider3()
        self.pushButton_dataproperties_apply_listener()

    def pushButton_dataproperties_apply_listener(self):
        self.dist_canvas.clearPlt()
        self.setPushButton_distrbution()


    def setCombox_Quadtree(self):
        vals = np.arange(2, 20, 1).astype('str').tolist()
        self.comboBox_Quadtree.addItems(vals)

    def directionCheckBoxHandler(self):
        """direction flag for checkbox
        * 0 for both
        * 1 for postive vector only
        * 2 for negative vector only
        * -1 if none selected
        """
        flag = -1
        postive_vector = self.checkBox_direction_positive.isChecked()
        negeative_vector = self.checkBox_direction_negative.isChecked()
        if (postive_vector and negeative_vector):
            flag = 0
            return flag
        elif (postive_vector):
            flag = 1
            return flag
        elif negeative_vector:
            flag = 2
            return flag
        else:
            flag = -1
            return flag

    def contentCheckBoxHandler(self):
        """content flag for checkbox
        * 0 for both
        * 1 for postive vector only
        * 2 for negative vector only
        * -1 if none selected
        """
        flag1 = -1
        contour = self.checkBox_content_contours.isChecked()
        vector = self.checkBox_content_vectors.isChecked()
        if (contour and vector):
            flag = 0
            return flag
        elif (contour):
            flag = 1
            return flag
        elif vector:
            flag = 2
            return flag
        else:
            flag = -1
            return flag

    def pushButton_mapproperties_apply_listener(self):
        # print(self.directionCheckBoxHandler())
        # print(self.contentCheckBoxHandler())
        # print(self.comboBox_Quadtree.currentIndex())
        self.setMapProperties()
        # def contentCheckBoxHandler(self):pass

    def setsHorizontalSliderMagnitude(self):
        pass

    def pushButton_mapproperties_reset_listener(self):
        print('Reset Listener')

    def setCheckBoxFillContours(self):
        self.canvas.setGeometry(QtCore.QRect(0, 0, 1011, 781))
        fillContours = self.checkBox_fill_contours.isChecked()
        if (fillContours):
            self.canvas.filledContour()
        else:
            self.canvas.clearPlt()
            self.canvas.spaghettiPlot()

    def setComboBoxColormapContours(self):
        pass

    def setHorizontalSliderOpacityContours(self):
        pass

    def setHorizontalSliderOpacityLines(self):
        pass

    def setcomboBoxColorLines(self):
        pass

    def setHorizontalSliderLineWidth(self):
        pass

    def setHorizontalSliderArrowWidth(self):
        pass

    def setHorizontalSliderArrowLength(self):
        pass
    def fileDialog(self):
        dialog = QFileDialog()
        filter = "*.csv"
        fileNames = QFileDialog.getOpenFileNames(dialog,"Open File",filter)
        if(len(fileNames[0]) > 0):
            self.processFilesNames(fileNames[0])
    def processFilesNames(self,fileNames):
        """Sort List based time line"""
        # fileNames = fileNames.sort()
        fileList = list()
        for i in range(len(fileNames)):
            fileName = fileNames[i].split("/")
            fileList.append(fileName[len(fileName) - 1])
            self.filenameToPathDict[fileName[len(fileName) - 1]] = fileNames[i]
        self.label_currentfile.setText(list(self.filenameToPathDict.keys())[0])
        observation_directory = list(self.filenameToPathDict.values())[0].split("/")[-3:-1]
        connector = "/"
        observation_directory = connector.join(observation_directory)
        self.label_obs_dir.setText(observation_directory)
    def setPushButton_distrbution(self):
        if(self.filenameToPathDict):
            file = list(self.filenameToPathDict.values())[0]
            self.dist_canvas.dist_plot(file,'SMOIS')
            self.dist_canvas.addVerticalLines(self.getcutOffValues()[0],self.getcutOffValues()[1],self.getcutOffValues()[2])
    def getcutOffValues(self):
        cut_off_point_1 = self.horizontalSlider_isoline1.value() / 100
        cut_off_point_2 = self.horizontalSlider_isoline2.value() / 100
        cut_off_point_3 = self.horizontalSlider_isoline3.value() / 100
        return [cut_off_point_1,cut_off_point_2,cut_off_point_3]
    def setMapProperties(self):
        levels = self.getcutOffValues()
        combobox_vals = np.arange(2, 100, 1).astype('str').tolist()
        quadTreeDepth_index = self.comboBox_Quadtree.currentIndex()
        magnitude_threshold = self.horizontalSlider_magnitude.value() / 100
        content_box = self.contentCheckBoxHandler()
        direction_box = self.directionCheckBoxHandler()
        quadTreeDepth = combobox_vals[quadTreeDepth_index]
        column = "SMOIS"
        self.drawContourMap(levels,content_box,direction_box,quadTreeDepth,column)

    def drawContourMap(self,levels,content_box,direction_box,quadTreeDepth,column):
        import matplotlib.pyplot as plt
        file_list = list(self.filenameToPathDict.values())
        data =  DataProcessing.importData(file_list[0])
        level = levels
        cntr_set = plt.contour(np.array(data['levels']).reshape(699, 639), level, colors=['g', 'r', 'y'])
        cntr_data = DataProcessing.modelTheGraph(cntr_set)
        weighted_graph = DataProcessing.createWeightedGraph(cntr_data, file_list, column)
        filtered_graph = DataProcessing.filterBasedOnGrid(100000, weighted_graph)
        GenerateImages.generateImages(filtered_graph, data, column)


    def generateImage(self):pass
        # file_list = list()
        # for i in range(len(list_of_files)):
        #     data = pd.read_csv('Dataset/' + list_of_files[i])[['longitude', 'latitude', column]]
        #     data.to_csv('Dataset/' + 'data' + str(i) + '.csv')
        #     file_list.append('Dataset/' + 'data' + str(i) + '.csv')
        # data = DataProcessing.importData(file_list[0])
        # data['levels'] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
        # levels = [0.25, 0.5, 0.75]
        # cntr_set = plt.contour(np.array(data['levels']).reshape(699, 639), levels, colors=['g', 'r', 'y'])
        # cntr_data = DataProcessing.modelTheGraph(cntr_set)
        # weighted_graph = DataProcessing.createWeightedGraph(cntr_data, file_list, column)
        # filtered_graph = DataProcessing.filterBasedOnGrid(100000, weighted_graph)
        # GenerateImages.generateImages(filtered_graph, data, column)

    def setHorizontalMagnitude(self):
        #value will be set according to the data
        self.horizontalSlider_magnitude.setMinimum(0)
        self.horizontalSlider_magnitude.setMaximum(100)
        self.horizontalSlider_magnitude.setTickInterval(1)
        self.horizontalSlider_magnitude.setValue(25)
        self.lineEdit_magnitude.setText(str(self.horizontalSlider_magnitude.value() / 100))
        self.horizontalSlider_magnitude.valueChanged.connect(self.setHorizontalMagnitudeListener)
    def setHorizontalMagnitudeListener(self):
        value = self.horizontalSlider_magnitude.value() / 100
        self.lineEdit_magnitude.setText(str(value))










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
