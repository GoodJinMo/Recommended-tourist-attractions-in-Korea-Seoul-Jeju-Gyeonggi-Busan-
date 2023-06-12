# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:21:15 2023

@author: USER
"""

#MyWindow.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
import sys
import pandas as pd
class MyWindow(QMainWindow):
    def __init__(self,title):
        super().__init__()
        font = QFont()
        font.setWeight(QFont.Bold)
        f=QFont()
        f.setFamily("HY중고딕") #
        f.setPointSize(14)
        #f.setWeight(QFont.Bold)
        
        
        f1=QFont()
        f1.setFamily("HY중고딕") 
        f1.setPointSize(8)
        
        fh=QFont()
        fh.setFamily("HY헤드라인M")
        fh.setPointSize(10)
        fh.setWeight(QFont.Bold)
        
        fc=QFont()
        fc.setFamily("HY엽서L") 
        fc.setPointSize(14)
        fc.setWeight(QFont.Bold)
        
        fg=QFont()
        fg.setFamily("HY견고딕")
        fg.setPointSize(10)
        fg.setWeight(QFont.Bold)
        
        style_sheet = "QListWidget { background-color: white; border: 2px solid black; }"
        style_sheet += "QListView::item { margin-bottom: 10px; }"
        
        self.setWindowIcon(QIcon('C:\work\python\miniapp\minisite\loc.png')) #loc.png 파일위치 loc.png=아이콘이미지
        self.setWindowTitle(title)
        self.resize(1900,1000)
        self.widget = QWidget() #Layout을 배치할 위젯 개체
        self.grid = QGridLayout(self.widget)
        self.setCentralWidget(self.widget)
        self.listfont=QFont('Arial',8)
        #%% #지역별 버튼 생성
        self.gb = QGroupBox("지역",self)
        self.gb.setStyleSheet("QGroupBox { background-color: white; border: 2px solid black; } QGroupBox:title { background-color: rgba(0, 0, 0, 0); padding:10px}")

        self.gb.setFont(fh)
        self.rb_grade1 = QRadioButton("경기",self.gb)
        self.rb_grade2 = QRadioButton("부산",self.gb)
        self.rb_grade3 = QRadioButton("서울",self.gb)
        self.rb_grade4 = QRadioButton("제주",self.gb)
        self.rb_grade5 = QRadioButton("강원",self.gb)
        self.rb_grade1.move(20,30)
        self.rb_grade2.move(100,30)
        self.rb_grade3.move(180,30)
        self.rb_grade4.move(60,60)
        self.rb_grade5.move(130,60)
        self.grid.addWidget(self.gb,0,0)
        self.rb_grade1.setChecked(True)
        self.rb_grade1.setFont(fg)
        self.rb_grade2.setFont(fg)
        self.rb_grade3.setFont(fg)
        self.rb_grade4.setFont(fg)
        self.rb_grade5.setFont(fg)
        self.rb_grade1.setStyleSheet('background-color:white')
        self.rb_grade2.setStyleSheet('background-color:white')
        self.rb_grade3.setStyleSheet('background-color:white')
        self.rb_grade4.setStyleSheet('background-color:white')
        self.rb_grade5.setStyleSheet('background-color:white')
        
       #%%  #마커표시하기,표시하지않기
        self.q=QGroupBox('마커표시',self)
        self.q.setStyleSheet("QGroupBox { background-color: white; border: 2px solid black; } QGroupBox:title { background-color: rgba(0, 0, 0, 0);padding: 10px; }")
        self.q.setFont(fh)
        self.null_mar=QPushButton("숨김",self.q)
        self.map_mar=QPushButton("생성",self.q)
        self.null_mar.move(30,50)
        self.map_mar.move(140,50)
        self.grid.addWidget(self.q,0,3)
        self.map_mar.setFont(fg)
        self.null_mar.setFont(fg)
        self.map_mar.clicked.connect(self.m_mar)
        self.null_mar.clicked.connect(self.n_mar)
        
      
        
       #%%  #검색 버튼 생성
        self.btn = QPushButton("검색")
        self.grid.addWidget(self.btn,1,0)
        self.btn.setStyleSheet("background-color:gray")
        self.btn.setFont(fg)
       #%%  #검색 리스트 생성
       
        ltext=QLabel('<List>')
        self.grid.addWidget(ltext,2,0)
        ltext.setFont(fh)
        self.lbox = QListWidget()
        self.grid.addWidget(self.lbox,3,0)
        self.lbox.setFont(self.listfont)
        
        self.lbox.setStyleSheet(style_sheet)
        self.lbox.setFont(f1)
       #%%  #마음 쏘옥 버튼 생성
        self.btn_kp = QPushButton("내 맴속에 저장")
        self.grid.addWidget(self.btn_kp,1,3)
        self.del_kp = QPushButton("내 맴속에서 나가")
        self.grid.addWidget(self.del_kp,2,3)
        
        self.btn_kp.setStyleSheet("background-color:gray")
        self.del_kp.setStyleSheet("background-color:gray")
        self.btn_kp.setFont(fg)
        self.del_kp.setFont(fg)
       #%%  #마음 쏘옥 리스트 생성
        
        self.lbox_kp = QListWidget()
        self.grid.addWidget(self.lbox_kp,3,3)
        self.lbox_kp.setFont(self.listfont)
        self.lbox_kp.setStyleSheet("QListView::item { margin-bottom: 10px; }")       
        self.lbox_kp.setStyleSheet(style_sheet)
       #%%  #사이트 가져오기
        self.webview = QWebEngineView()
        self.grid.addWidget(self.webview,0,1,5,1)
        self.webview.load(QUrl('http://localhost/minisite/site.html')) #사이트 주소 iir minisite.html 등록 후 주소 가져오기
       
        #%% info
        self.inin=QGroupBox("",self)
        self.info = QGroupBox("",self.inin)
        
        
        self.info.setFixedSize(810, 500)
        self.info.move(0,230)
        self.inin.setVisible(False)
        self.inin.setStyleSheet('background-color:rgba(0, 0, 0, 0)')
        self.info.setStyleSheet("QGroupBox { background-color: white; border: 2px solid black;border-width: 5px 5px 2px 5px; border-style: solid; }")
        
        lb_line4=QLabel(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",self.info)
        lb_line4.move(20,30)
        lb_line4.setStyleSheet('background-color: rgba(255, 255, 255, 0); color: rgba(0, 0, 0, 64);')
              
        lb_nick=QLabel("이름:",self.info)     
        lb_nick.setFont(f)
        lb_nick.move(20,50)
        self.nick=QLabel(" ",self.info)
        self.nick.resize(500,50)
        self.nick.move(80,35)
        lb_nick.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.nick.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.nick.setFont(f)
        
        lb_vl=QLabel("",self.info)
        lb_vl.move(20,100)
        lb_vl.setFont(f)
        self.vl=QLabel("    ",self.info)
        self.vl.move(80,85)
        self.vl.resize(500,50)
        lb_vl.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.vl.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.vl.setFont(f)
        
        lb_line=QLabel("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",self.info)
        lb_line.move(20,120)
        lb_line.setStyleSheet('background-color: rgba(255, 255, 255, 0); color: rgba(0, 0, 0, 64);')
                              
        lb_st=QLabel("주소:",self.info)
        lb_st.move(20,150)
        lb_st.setFont(f)
        self.sta=QLabel("",self.info)
        self.sta.move(80,135)
        self.sta.resize(600,50)
        lb_st.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.sta.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.sta.setFont(f)
        lb_line1=QLabel("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",self.info)
        lb_line1.move(20,170)
        lb_line1.setStyleSheet('background-color: rgba(255, 255, 255, 0); color: rgba(0, 0, 0, 64);')
              
        
        lb_ph=QLabel("전화번호:",self.info)
        lb_ph.move(20,200)
        lb_ph.setFont(f)
        self.pha=QLabel(" ",self.info)
        self.pha.move(130,185)
        self.pha.resize(500,50)
        lb_ph.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.pha.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.pha.setFont(f)
        lb_line2=QLabel("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",self.info)
        lb_line2.move(20,220)
        lb_line2.setStyleSheet('background-color: rgba(255, 255, 255, 0); color: rgba(0, 0, 0, 64);')
              
        
        lb_con=QLabel("<내용>",self.info)
        lb_con.move(20,250)
        lb_con.setFont(f)
        self.cona=QLabel("",self.info)
        self.cona.move(20,280)
        self.cona.resize(780,200)
        self.cona.setWordWrap(True) 
        self.cona.setAlignment(Qt.AlignTop)
        lb_con.setStyleSheet('background-color:rgba(255, 255, 255, 0)')
        self.cona.setStyleSheet('background-color:rgba(255, 255, 255, 0);padding: 10px;')
        self.cona.setFont(f)
        
        self.del_btn=QPushButton("x",self.info)
        self.del_btn.move(770,10)
        self.del_btn.resize(30,30)
        self.del_btn.setStyleSheet('background-color:gray;')
        self.grid.addWidget(self.inin,3,1,1,1)
        self.del_btn.clicked.connect(self.del_info)
       #%%  #크기정하기
        self.grid.setRowStretch(0,3)
        self.grid.setRowStretch(1,1)
        self.grid.setRowStretch(3,15)
        self.grid.setColumnStretch(1,15)
        
       #%%  #검색버튼 검색함수 연결
        self.btn.clicked.connect(self.btn_clicked)
        #검색리스트 리스트개체 클릭 연결
        self.lbox.currentItemChanged.connect(self.lbox_ch_selected)
        self.lbox.itemDoubleClicked.connect(self.lbox_dou_sel)
        
     #%%    #마음쏘옥 버튼 함수 연결
        self.btn_kp.clicked.connect(self.btn_kp_clicked)
        self.del_kp.clicked.connect(self.del_kp_clicked)
        self.lbox_kp.currentItemChanged.connect(self.lbox_ch_kp_selected)
        self.lbox_kp.itemDoubleClicked.connect(self.lbox_kp_dou_sel)
     #%%    #초기값 설정
        self.kp=[]
        self.row = -1
        self.hom=""
        
     #%%    #액셀 가져오기
        self.dt=[pd.read_excel("C:\work\python\miniapp\minisite\경기.xlsx"),
                 pd.read_excel("C:\work\python\miniapp\minisite\부산좌표.xlsx"),
                 pd.read_excel("C:\work\python\miniapp\minisite\서울_예린.xlsx"),
                 pd.read_excel("C:\work\python\miniapp\minisite\제주.xlsx")]
  #%% 함수 
    def openNewWindow(self):
        
        new_window = MyWindow()
        new_window.show()

        url = self.hom  # 원하는 URL로 변경
        new_webview = QWebEngineView(new_window)
        new_webview.load(QUrl(url))
        new_window.setCentralWidget(new_webview)
        
        
        
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "확인", "정말로 창을 닫으시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
  
    def del_info(self):
        self.inin.setVisible(False)
        
    def kp_infoset(self):
        drow=self.lbox_kp.currentRow()
        self.nick.setText(self.kp[drow][2]+" ("+self.kp[drow][8]+")")
        self.vl.setText(self.kp[drow][6])
        self.sta.setText(self.kp[drow][3])
        self.pha.setText(self.kp[drow][4])
        self.cona.setText(self.kp[drow][7])
        
    def infoset(self):
        self.nick.setText(self.title[self.row]+" ("+self.key[self.row]+")")
        self.vl.setText(self.val[self.row])
        self.sta.setText(self.an[self.row])
        self.pha.setText(self.ph[self.row])
        self.cona.setText(self.con[self.row])
        #검색 함수
    #마음쏘옥저장
    def btn_kp_clicked(self):
        
        if self.row==-1:
            return
        
        item = self.lbox.item(self.row)
        item.setBackground(QColor(250, 244, 192))
        
        ti=self.title[self.row]
        x = self.long[self.row]
        y = self.lat[self.row]
        an=self.an[self.row]
        ph=self.ph[self.row]
        vl=self.val[self.row]
        con=self.con[self.row]
        key=self.key[self.row]
        self.kp.append([x,y,ti,an,ph,self.row,vl,con,key])
        self.lbox_kp.addItem("("+self.key[self.row]+") "+ti) #리스트 요소 추가
        
        #마음쏘옥 삭제
    def del_kp_clicked(self):
        drow=self.lbox_kp.currentRow()
        if drow == -1:
            return
        self.lbox_kp.takeItem(drow)
        item = self.lbox.item(self.kp[drow][5])
        item.setBackground(QColor(255, 255, 255))
        del self.kp[drow]
        
        #마음쏘옥 리스트 요소 클릭
    def lbox_ch_kp_selected(self):
        
        rowkp = self.lbox_kp.currentRow()
        if rowkp == -1:
            return
        self.kp_infoset()
        page = self.webview.page()
        script = f'setMove({self.kp[rowkp][1]},{self.kp[rowkp][0]},{self.kp[rowkp][5]})'
        page.runJavaScript(script)
        self.lbox.setCurrentItem(None)
        #리스트 요소 클릭
    def lbox_ch_selected(self):
        
        self.row = self.lbox.currentRow()
        
        if self.row == -1:
            return
        x = self.long[self.row]
        y = self.lat[self.row]
        
        self.infoset()
        page = self.webview.page()
        
        script = f'setMove({y},{x},{self.row})'
        page.runJavaScript(script)
        self.lbox_kp.setCurrentItem(None)
        #더블클릭
    def lbox_dou_sel(self):
        self.row = self.lbox.currentRow()
        if self.row == -1:
            return
        self.inin.setVisible(True)
        self.infoset()
    def lbox_kp_dou_sel(self):
        drow = self.lbox_kp.currentRow()
        if drow == -1:
            return
        self.inin.setVisible(True)
        self.kp_infoset()
    
    #마커 보였다,안보였다!
    def m_mar(self):
        page = self.webview.page()
        script =f'markercon({2})'
        page.runJavaScript(script)
        
    def n_mar(self):
        page = self.webview.page()
        script =f'markercon({1})'
        page.runJavaScript(script)
        
   
        
    #검색 버튼
    def btn_clicked(self):

        dd = self.get_grade() #해당하는 지역 데이터 가져오기
        
        self.lbox.clear()   #리스트 초기화
        self.lbox_kp.clear()
        
        # 가져오기
        self.title=list(dd.to_dict()[dd.columns[0]].values())
        self.lat=list(dd.to_dict()[dd.columns[3]].values())
        self.long=list(dd.to_dict()[dd.columns[4]].values())
        self.an=list(dd.to_dict()[dd.columns[1]].values())
        self.ph=list(dd.to_dict()[dd.columns[2]].values())
        self.st=list(dd.to_dict()[dd.columns[5]].values())
        self.key=list(dd.to_dict()[dd.columns[6]].values())
        self.val=list(dd.to_dict()[dd.columns[7]].values())
        self.con=list(dd.to_dict()[dd.columns[8]].values())
        self.img=[]
        
        for i,n in enumerate(self.key):  #항목에맞는 이미지 가져오기
            self.lbox.addItem("("+n+") "+self.title[i])
            if n=="숙소":
                self.img.append("https://ifh.cc/g/Mm55t3.png")
            elif n=="음식":
                self.img.append("https://ifh.cc/g/VzGQtO.png")
            else:
                self.img.append("https://ifh.cc/g/B1clh9.png")
        self.kp=[]
        
        #자바스크립트 함수 실행
        page = self.webview.page()
        script = f'setCenter({self.lat},{self.long},{self.title},{self.img},{self.an},{self.ph},{self.st})'
        page.runJavaScript(script)
  
    #이게맞나 지역
    def get_grade(self):
        if self.rb_grade1.isChecked():
            return self.dt[0]
        if self.rb_grade2.isChecked():
            return self.dt[1]
        if self.rb_grade3.isChecked():
            return self.dt[2]
        if self.rb_grade4.isChecked():
            return self.dt[3]

