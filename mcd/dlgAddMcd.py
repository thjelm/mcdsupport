# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcd\dlgAddMcd.ui'
#
# Created: Wed Sep 07 02:06:50 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "New cloze cards", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setText(QtGui.QApplication.translate("Dialog", "Phrase / Passage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.selectionEdit = QtGui.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.selectionEdit.setFont(font)
        self.selectionEdit.setTabChangesFocus(True)
        self.selectionEdit.setObjectName(_fromUtf8("selectionEdit"))
        self.verticalLayout_2.addWidget(self.selectionEdit)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.notesEdit = QtGui.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.notesEdit.setFont(font)
        self.notesEdit.setTabChangesFocus(True)
        self.notesEdit.setObjectName(_fromUtf8("notesEdit"))
        self.verticalLayout_2.addWidget(self.notesEdit)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout_2.setStretch(3, 4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Clozes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.clozesEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clozesEdit.sizePolicy().hasHeightForWidth())
        self.clozesEdit.setSizePolicy(sizePolicy)
        self.clozesEdit.setObjectName(_fromUtf8("clozesEdit"))
        self.horizontalLayout_3.addWidget(self.clozesEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.modellabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modellabel.sizePolicy().hasHeightForWidth())
        self.modellabel.setSizePolicy(sizePolicy)
        self.modellabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.modellabel.setText(QtGui.QApplication.translate("Dialog", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.modellabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modellabel.setObjectName(_fromUtf8("modellabel"))
        self.horizontalLayout.addWidget(self.modellabel)
        self.tagslineedit = TagEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagslineedit.sizePolicy().hasHeightForWidth())
        self.tagslineedit.setSizePolicy(sizePolicy)
        self.tagslineedit.setObjectName(_fromUtf8("tagslineedit"))
        self.horizontalLayout.addWidget(self.tagslineedit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tagslabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagslabel.sizePolicy().hasHeightForWidth())
        self.tagslabel.setSizePolicy(sizePolicy)
        self.tagslabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tagslabel.setText(QtGui.QApplication.translate("Dialog", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.tagslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tagslabel.setObjectName(_fromUtf8("tagslabel"))
        self.horizontalLayout_4.addWidget(self.tagslabel)
        self.modelcombobox = QtGui.QComboBox(Dialog)
        self.modelcombobox.setObjectName(_fromUtf8("modelcombobox"))
        self.horizontalLayout_4.addWidget(self.modelcombobox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.statusLabel = QtGui.QLabel(Dialog)
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout_5.addWidget(self.statusLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.configbutton = QtGui.QPushButton(Dialog)
        self.configbutton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configbutton.sizePolicy().hasHeightForWidth())
        self.configbutton.setSizePolicy(sizePolicy)
        self.configbutton.setText(QtGui.QApplication.translate("Dialog", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.configbutton.setCheckable(False)
        self.configbutton.setObjectName(_fromUtf8("configbutton"))
        self.horizontalLayout_2.addWidget(self.configbutton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout_2.addWidget(self.addButton)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.selectionEdit, self.notesEdit)
        Dialog.setTabOrder(self.notesEdit, self.clozesEdit)
        Dialog.setTabOrder(self.clozesEdit, self.tagslineedit)
        Dialog.setTabOrder(self.tagslineedit, self.modelcombobox)
        Dialog.setTabOrder(self.modelcombobox, self.configbutton)
        Dialog.setTabOrder(self.configbutton, self.addButton)
        Dialog.setTabOrder(self.addButton, self.buttonBox)

    def retranslateUi(self, Dialog):
        pass

from ankiqt.ui.tagedit import TagEdit
