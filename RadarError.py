# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\薛志远\eric6\test.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

dict = {
            'X1':'励磁监控继电器损坏。', 
            'X2':'变频器T3损坏。', 
            'X3':'线路中发生开路，例如保险丝FU1，整流桥U1，电阻R1。', 
            'X4':'线路中发生局部开路，例如保险丝FU1，整流桥U1，电阻R1。', 
            'X5':'钛泵监控继电器损坏，输出故障指示', 
            'X6':'速调管内有空气。', 
            'X7':'钛泵产生电路中局部短路。', 
            'X8':'收发机柜门没有闭合。', 
            'X9':'调制器打火严重。', 
            'X10':'控保继电器K2的9，10脚损坏，输出故障指示。', 
            'X11':'调制器IGBT模块损坏。', 
            'X12':'控保电路中调制脉冲测试电路局部短路。', 
            'X13':'控保继电器K2的6，7脚损坏，输出故障指示。', 
            'X14':'预调脉冲产生电路局部短路。', 
            'X15':'控保电路中预调脉冲测试电路局部短路。', 
            'X16':'预调器中变压器T1的5，6脚损坏。', 
            'X17':'中压保护继电器损坏，开关K3断开。', 
            'X18':'150V产生电路中发生开路，如保险丝FU3断开。', 
            'X19':'预调器中变压器T1的1，2脚损坏。', 
            'X20':'加电电路发生开路，如保险丝FU1断开。', 
            'X21':'预调器中变压器T1的3，4脚损坏。', 
            'X22':'交流15V产生电路和净化电源电路中发生开路，如保险丝FU2断开。', 
            'X23':'控保电路中预调脉冲测试电路发生开路。', 
            'X24':'预调脉冲产生电路中发生开路。', 
            'X25':'控保继电器K4的5,6脚损坏，输出故障指示。', 
            'X26':'控保继电器K1损坏，6，7脚和9，10脚输出故障指示。', 
            'X27':'信号处理器中定时器损坏，未产生触发脉冲。', 
            'X28':'外触发产生电路开路。', 
            'X29':'NE555同步定时器损坏。', 
            'X30':'内触发产生电路开路。', 
            'X31':'变压器T2的8，13脚损坏。', 
            'X32':'灯丝监控继电器损坏，输出故障指示。', 
            'X33':'灯丝电路中局部开路，例如保险丝FU3，电感TA1。', 
            'X34':'缓起动继电器无动作。', 
            'X35':'变压器T2的10脚损坏。', 
            'X36':'速调管内部发生短路。', 
            'X37':'软波导人为连接不恰当。', 
            'X38':'馈线系统中波导开关故障。', 
            'X39':'波导系统密封故障。', 
            'X40':'PLC芯片损坏。', 
            'X41':'PLC的Y15准加指示接口损坏。', 
            'X42':'检波器故障。', 
            'X43':'连接电缆没有接好。', 
            'X44':'高压整流器开路。', 
            'X45':'没有3200V输出。', 
            'X46':'储能电容短路，无法放电。', 
            'X47':'速调管内磁控管灯丝开路。', 
            'X48':'可控硅完全损坏，导致调至脉冲波形与激励脉冲在时序上完全错位。', 
            'X49':'频综器损坏。', 
            'X50':'信号处理器中定时器损坏，未产生激励脉冲。', 
            'X51':'可变衰减器损坏。', 
            'X52':'功率放大器损坏。', 
            'X53':'工作电压12V未加。', 
            'X54':'高压缓冲延时继电器K1和K2损坏，只有半高压。', 
            'X55':'高压整流器中变压器损坏，输出电压远小于3200V。',
            'X56':'储能电容漏电或被击穿短路。',
            'X57':'速调管内磁控管寿命期到。',
            'X58':'可控硅部分损坏，导致调制脉冲波形与激励脉冲在时序上重合度不高。', 
            'X59':'功率放大器寿命期到！',  
                       }

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 763)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.shuchugonglvxiao = QtWidgets.QTabWidget(self.centralWidget)
        self.shuchugonglvxiao.setGeometry(QtCore.QRect(20, 30, 1081, 711))
        self.shuchugonglvxiao.setObjectName("shuchugonglvxiao")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 1041, 651))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.verticalLayoutWidget_2)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout_2.addWidget(self.treeWidget_2)
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.verticalLayout_2.addWidget(self.textBrowser_1)
        self.shuchugonglvxiao.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1041, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.treeWidget)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.shuchugonglvxiao.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 1041, 651))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.verticalLayoutWidget_3)
        self.treeWidget_3.setObjectName("treeWidget_3")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        self.verticalLayout_3.addWidget(self.treeWidget_3)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_3.addWidget(self.textBrowser_3)
        self.shuchugonglvxiao.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.shuchugonglvxiao.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.treeWidget_2.itemSelectionChanged.connect(self.refresh1)
        self.treeWidget.itemSelectionChanged.connect(self.refresh2)
        self.treeWidget_3.itemSelectionChanged.connect(self.refresh3)

    def refresh1(self):
        try:
            item = self.treeWidget_2.selectedItems()
            s = str(item[0].text(0))
            self.textBrowser_1.setText(dict[s])
        except:
            pass
            
    def refresh2(self):
        try:
            item = self.treeWidget.selectedItems()
            s = str(item[0].text(0))
            self.textBrowser_2.setText(dict[s])
        except:
            pass
    
    def refresh3(self):
        try:
            item = self.treeWidget_3.selectedItems()
            s = str(item[0].text(0))
            self.textBrowser_3.setText(dict[s])
        except:
            pass
            
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "故障树诊断"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "T1  雷达正常开机后，低压通，延时10分钟后，准加指示灯不亮，加不上高压"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "E1  励磁故障"))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "X1"))
        self.treeWidget_2.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "X2"))
        self.treeWidget_2.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "X3"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "E2  软泵故障"))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "E9  无软泵电流"))
        self.treeWidget_2.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "X4"))
        self.treeWidget_2.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "E10  软泵电流过大"))
        self.treeWidget_2.topLevelItem(1).child(1).child(0).setText(0, _translate("MainWindow", "X5"))
        self.treeWidget_2.topLevelItem(1).child(1).child(1).setText(0, _translate("MainWindow", "X6"))
        self.treeWidget_2.topLevelItem(1).child(1).child(2).setText(0, _translate("MainWindow", "X7"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("MainWindow", "E3  门开关故障"))
        self.treeWidget_2.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "X8"))
        self.treeWidget_2.topLevelItem(3).setText(0, _translate("MainWindow", "E4  调制脉冲故障"))
        self.treeWidget_2.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "E11  调制脉冲过流"))
        self.treeWidget_2.topLevelItem(3).child(0).child(0).setText(0, _translate("MainWindow", "X9"))
        self.treeWidget_2.topLevelItem(3).child(0).child(1).setText(0, _translate("MainWindow", "X10"))
        self.treeWidget_2.topLevelItem(3).child(0).child(2).setText(0, _translate("MainWindow", "X11"))
        self.treeWidget_2.topLevelItem(3).child(0).child(3).setText(0, _translate("MainWindow", "X12"))
        self.treeWidget_2.topLevelItem(3).child(0).child(4).setText(0, _translate("MainWindow", "E14  预调脉冲故障"))
        self.treeWidget_2.topLevelItem(3).child(0).child(4).child(0).setText(0, _translate("MainWindow", "X13"))
        self.treeWidget_2.topLevelItem(3).child(0).child(4).child(1).setText(0, _translate("MainWindow", "X14"))
        self.treeWidget_2.topLevelItem(3).child(0).child(4).child(2).setText(0, _translate("MainWindow", "X15"))
        self.treeWidget_2.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "E12  预调脉冲故障"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).setText(0, _translate("MainWindow", "E15  电源故障"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(0).setText(0, _translate("MainWindow", "E18  没有150V电压"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(0).child(0).setText(0, _translate("MainWindow", "X16"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(0).child(1).setText(0, _translate("MainWindow", "X17"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(0).child(2).setText(0, _translate("MainWindow", "X18"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(1).setText(0, _translate("MainWindow", "E19  没有交流220V电压"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(1).child(0).setText(0, _translate("MainWindow", "X19"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(1).child(1).setText(0, _translate("MainWindow", "X20"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(2).setText(0, _translate("MainWindow", "E20  没有12V电压"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(2).child(0).setText(0, _translate("MainWindow", "X21"))
        self.treeWidget_2.topLevelItem(3).child(1).child(0).child(2).child(1).setText(0, _translate("MainWindow", "X22"))
        self.treeWidget_2.topLevelItem(3).child(1).child(1).setText(0, _translate("MainWindow", "E16  预调脉冲产生电路和监控电路故障"))
        self.treeWidget_2.topLevelItem(3).child(1).child(1).child(0).setText(0, _translate("MainWindow", "X23"))
        self.treeWidget_2.topLevelItem(3).child(1).child(1).child(1).setText(0, _translate("MainWindow", "X24"))
        self.treeWidget_2.topLevelItem(3).child(1).child(1).child(2).setText(0, _translate("MainWindow", "X25"))
        self.treeWidget_2.topLevelItem(3).child(1).child(1).child(3).setText(0, _translate("MainWindow", "X26"))
        self.treeWidget_2.topLevelItem(3).child(1).child(2).setText(0, _translate("MainWindow", "E17  无内外触发输入"))
        self.treeWidget_2.topLevelItem(3).child(1).child(2).child(0).setText(0, _translate("MainWindow", "E21  外触发故障"))
        self.treeWidget_2.topLevelItem(3).child(1).child(2).child(0).child(0).setText(0, _translate("MainWindow", "X27"))
        self.treeWidget_2.topLevelItem(3).child(1).child(2).child(0).child(1).setText(0, _translate("MainWindow", "X28"))
        self.treeWidget_2.topLevelItem(3).child(1).child(2).child(1).setText(0, _translate("MainWindow", "E22  内触发故障"))
        self.treeWidget_2.topLevelItem(3).child(1).child(2).child(1).child(0).setText(0, _translate("MainWindow", "X29"))
        self.treeWidget_2.topLevelItem(3).child(1).child(2).child(1).child(1).setText(0, _translate("MainWindow", "X30"))
        self.treeWidget_2.topLevelItem(4).setText(0, _translate("MainWindow", "E5  灯丝欠流故障"))
        self.treeWidget_2.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "X31"))
        self.treeWidget_2.topLevelItem(4).child(1).setText(0, _translate("MainWindow", "X32"))
        self.treeWidget_2.topLevelItem(4).child(2).setText(0, _translate("MainWindow", "X33"))
        self.treeWidget_2.topLevelItem(4).child(3).setText(0, _translate("MainWindow", "X34"))
        self.treeWidget_2.topLevelItem(5).setText(0, _translate("MainWindow", "E6  注电流故障"))
        self.treeWidget_2.topLevelItem(5).child(0).setText(0, _translate("MainWindow", "X35"))
        self.treeWidget_2.topLevelItem(5).child(1).setText(0, _translate("MainWindow", "X36"))
        self.treeWidget_2.topLevelItem(6).setText(0, _translate("MainWindow", "E7  软波导故障"))
        self.treeWidget_2.topLevelItem(6).child(0).setText(0, _translate("MainWindow", "X37"))
        self.treeWidget_2.topLevelItem(6).child(1).setText(0, _translate("MainWindow", "E13  波导机械故障"))
        self.treeWidget_2.topLevelItem(6).child(1).child(0).setText(0, _translate("MainWindow", "X38"))
        self.treeWidget_2.topLevelItem(6).child(1).child(1).setText(0, _translate("MainWindow", "X39"))
        self.treeWidget_2.topLevelItem(7).setText(0, _translate("MainWindow", "E8  PLC故障"))
        self.treeWidget_2.topLevelItem(7).child(0).setText(0, _translate("MainWindow", "X40"))
        self.treeWidget_2.topLevelItem(7).child(1).setText(0, _translate("MainWindow", "X41"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.shuchugonglvxiao.setTabText(self.shuchugonglvxiao.indexOf(self.tab_2), _translate("MainWindow", "加不上高压"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "T3  加高压后，输出功率小于正常值（功率电平指示偏小）"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "E30  高压偏小"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "X54"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "X55"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "X56"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "E31  速调管故障"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "X57"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "X58"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "E32  功放输出偏小"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "X59"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.shuchugonglvxiao.setTabText(self.shuchugonglvxiao.indexOf(self.tab), _translate("MainWindow", "输出功率小"))
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "T2  加高压后无输出功率（无功率电平指示）"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("MainWindow", "E23  接收到回波，但无发射功率电平显示"))
        self.treeWidget_3.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "X42"))
        self.treeWidget_3.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "X43"))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("MainWindow", "E24  没有回波"))
        self.treeWidget_3.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "E25  高压电路问题"))
        self.treeWidget_3.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "X44"))
        self.treeWidget_3.topLevelItem(1).child(0).child(1).setText(0, _translate("MainWindow", "X45"))
        self.treeWidget_3.topLevelItem(1).child(0).child(2).setText(0, _translate("MainWindow", "X46"))
        self.treeWidget_3.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "E26  速调管故障"))
        self.treeWidget_3.topLevelItem(1).child(1).child(0).setText(0, _translate("MainWindow", "X47"))
        self.treeWidget_3.topLevelItem(1).child(1).child(1).setText(0, _translate("MainWindow", "X48"))
        self.treeWidget_3.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "E27  没有功放输出"))
        self.treeWidget_3.topLevelItem(1).child(2).child(0).setText(0, _translate("MainWindow", "E28  无励磁脉冲信号"))
        self.treeWidget_3.topLevelItem(1).child(2).child(0).child(0).setText(0, _translate("MainWindow", "X49"))
        self.treeWidget_3.topLevelItem(1).child(2).child(0).child(1).setText(0, _translate("MainWindow", "X50"))
        self.treeWidget_3.topLevelItem(1).child(2).child(1).setText(0, _translate("MainWindow", "E29  功放分机故障"))
        self.treeWidget_3.topLevelItem(1).child(2).child(1).child(0).setText(0, _translate("MainWindow", "X51"))
        self.treeWidget_3.topLevelItem(1).child(2).child(1).child(1).setText(0, _translate("MainWindow", "X52"))
        self.treeWidget_3.topLevelItem(1).child(2).child(1).child(2).setText(0, _translate("MainWindow", "X53"))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.shuchugonglvxiao.setTabText(self.shuchugonglvxiao.indexOf(self.tab_3), _translate("MainWindow", "无输出功率"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

