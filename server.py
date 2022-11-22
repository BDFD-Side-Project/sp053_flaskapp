# This is the flask server of waterfrontes.com
# This is test message for updating
#coding: UTF-8
# -*- coding: UTF-8 -*- 
# coding=utf-8 

# from distutils.log import debpytug
from flask import Flask, send_file, redirect, render_template, url_for, request, flash
# import math
# import sys
import WES_Calculation as wes


# import matplotlib
# import PyQt5
# matplotlib.rc("font",family='FangSong')
# matplotlib.use('Agg')
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# from matplotlib.ticker import FixedLocator, FixedFormatter
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# import seaborn as sns
# import numpy as np
#import sys # (20211226)
# from numpy import *
# from decimal import Decimal
# import io
# import base64
# import statistics

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/guide.html")
def guide():
    return render_template("guide.html")

@app.route("/disclaim.html")
def disclaim():
    return render_template("disclaim.html")

@app.route("/test")
def test():
    return render_template("instructions/gumbelhelp2.html")

@app.route("/greenampthelp.html")
def greenampthelp():
    return render_template("instructions/greenampthelp.html")

@app.route("/greenamptupdate.html")
def greenamptupdate():
    return render_template("updates/greenamptupdate.html")

@app.route("/gumbelhelp.html")
def gumbelhelp():
    return render_template("instructions/gumbelhelp.html")

@app.route("/gumbelupdate.html")
def gumbelupdate():
    return render_template("updates/gumbelupdate.html")

@app.route("/wavespectrahelp.html")
def wavespectrahelp():
    return render_template("instructions/wavespectrahelp.html")

@app.route("/wavespectraupdate.html")
def wavespectraupdate():
    return render_template("updates/wavespectraupdate.html")

@app.route("/wavespectra.html", methods=["POST", "GET"])
def wavespectra():
    if request.method == "POST":
        c1 = int(request.form["radio"])
        d_1, X_1, U_1, el_1, gamma_1, Hs_1, Tz_1, Ts_1 = "","","","","","","",""
        X_2, X_2_Replace, U_2, el_2, gamma_2, Hs_2, Tz_2, Ts_2, Tp_2 = "","","","","","","","",""
        mingzi = request.form["mingzi"]
        # If c1=1, please input the following paramaters:
        if c1 == 1:
            d_1 = (request.form["d"])   # water depth (m)
            if not d_1:
                d_1 = ""
                d = None
            else:
                d_1 = d_1
                d = float(d_1)           
            X_1 = request.form["X_1"]
            if not X_1:
                X_1 = ""
                X = None
            else:
                X_1 = X_1
                X = float(X_1)*1000                
            # U = float(request.form["U_1"])  # wind speed (m/s)
            U_1 = (request.form["U_1"])  # wind speed (m/s)
            if not U_1:
                U_1 = ""
                U = None
            else:
                U_1 = U_1
                U = float(U_1)                
            # el = float(request.form["el_1"])   # the elevation of the wind speed (m)      
            el_1 = (request.form["el_1"])   # the elevation of the wind speed (m)
            if not el_1:
                el_1 = ""
                el = None
            else:
                el_1 = el_1
                el = float(el_1)                   
            # gamma = float(request.form["gamma_1"])   # peakedness parameter for JONSWAP (between 1 and 7, but 3.30 is normally recommended)
            gamma_1 = (request.form["gamma_1"])   # peakedness parameter for JONSWAP (between 1 and 7, but 3.30 is normally recommended)
            if not gamma_1:
                gamma_1 = ""
                gamma = None
            else:
                gamma_1 = gamma_1
                gamma = float(gamma_1)  
            # Hs = float(request.form["Hs_1"])   # significant wave height (m)
            Hs_1 = (request.form["Hs_1"])   # significant wave height (m)
            if not Hs_1:
                Hs_1 = ""
                Hs = None
            else:
                Hs_1 = Hs_1
                Hs = float(Hs_1)  
            # Tz = float(request.form["Tz_1"])  # average zero-crossing period from data (s)
            Tz_1 = (request.form["Tz_1"])  # average zero-crossing period from data (s)
            if not Tz_1:
                Tz_1 = ""
                Tz = None
            else:
                Tz_1 = Tz_1
                Tz = float(Tz_1)  
            Ts_1 = request.form["Ts_1"] # significant wave period (s)
            if not Ts_1:
                Ts_1 = ""
                Ts = None
            else:
                Ts_1 = Ts_1
                Ts = float(Ts_1) 
            # Ts = request.form["Ts_1"] # significant wave period (s)
            # Ts = data_service.data_conv(Ts)
            Tp = None

        # If c1=2, please input the following paramaters:
        if c1 == 2:
            X_2 = request.form["X_2"]
            if X_2 == "None":
                X_2_Replace = "不考虑"
                X_2 = "None"
                X = None
            else:
                X_2 = X_2
                X = float(X_2)*1000                
            U_2 = (request.form["U_2"])  # wind speed (m/s)
            if not U_2:
                U_2 = ""
                U = None
            else:
                U_2 = U_2
                U = float(U_2)                
            # el = float(request.form["el_1"])   # the elevation of the wind speed (m)      
            el_2 = (request.form["el_2"])   # the elevation of the wind speed (m)
            if not el_2:
                el_2 = ""
                el = None
            else:
                el_2 = el_2
                el = float(el_2)                   
            # gamma = float(request.form["gamma_1"])   # peakedness parameter for JONSWAP (between 1 and 7, but 3.30 is normally recommended)
            gamma_2 = (request.form["gamma_2"])   # peakedness parameter for JONSWAP (between 1 and 7, but 3.30 is normally recommended)
            if not gamma_2:
                gamma_2 = ""
                gamma = None
            else:
                gamma_2 = gamma_2
                gamma = float(gamma_2)  
            # Hs = float(request.form["Hs_1"])   # significant wave height (m)
            Hs_2 = (request.form["Hs_2"])   # significant wave height (m)
            if not Hs_2:
                Hs_2 = ""
                Hs = None
            else:
                Hs_2 = Hs_2
                Hs = float(Hs_2)  
            # Tz = float(request.form["Tz_1"])  # average zero-crossing period from data (s)
            Tz_2 = (request.form["Tz_2"])  # average zero-crossing period from data (s)
            if not Tz_2:
                Tz_2 = ""
                Tz = None
            else:
                Tz_2 = Tz_2
                Tz = float(Tz_2)  
            Ts_2 = request.form["Ts_2"] # significant wave period (s)
            if not Ts_2:
                Ts_2 = ""
                Ts = None
            else:
                Ts_2 = Ts_2
                Ts = float(Ts_2) 
            Tp_2 = request.form["Tp"] # significant wave period (s)
            if not Tp_2:
                Tp_2 = ""
                Tp = None
            else:
                Tp_2 = Tp_2
                Tp = float(Tp_2) 
            d = None       

        img_stream, heading, data1, data1_heading, data2, data2_heading, content, ending = wes.wave(c1, d, X, U, el, gamma, Hs, Tz, Ts, Tp)
        # return render_template("wave.html", img_stream=img_stream, heading=heading, data1=data1, data1_heading1=data1_heading1, data1_heading2=data1_heading2, data2=data2, data2_heading1=data2_heading1, data2_heading2=data2_heading2, content=content, ending=ending )
        # print(c1,X_2,U_2,el_2,gamma_2,Hs_2,Tz_2,Ts_2,Tp_2)
        # print(d,X,U,el,gamma,Hs,Tz,Ts)
        return render_template("wavespectra.html",mingzi=mingzi,d_1=d_1,X_1=X_1,U_1=U_1,el_1=el_1,gamma_1=gamma_1,Hs_1=Hs_1,Tz_1=Tz_1,Ts_1=Ts_1,c1=c1,X_2=X_2,X_2_Replace=X_2_Replace,U_2=U_2,el_2=el_2,gamma_2=gamma_2,Hs_2=Hs_2,Tz_2=Tz_2,Ts_2=Ts_2,Tp_2=Tp_2,img_stream=img_stream, heading=heading, data1=data1, data1_heading=data1_heading, data2=data2, data2_heading=data2_heading, content=content, ending=ending )
        # return render_template("wavetest.html", d_1=d_1,X_1=X_1,U_1=U_1,el_1=el_1,gamma_1=gamma_1,Hs_1=Hs_1,Tz_1=Tz_1,Ts_1=Ts_1,c1=c1,X_2=X_2,U_2=U_2,el_2=el_2,gamma_2=gamma_2,Hs_2=Hs_2,Tz_2=Tz_2,Ts_2=Ts_2,Tp_2=Tp_2)
    else:
        return render_template("wavespectra.html",c1=1)

@app.route("/wave1", methods=["POST", "GET"])
def wave():
    if request.method == "POST":
        c1 = int(request.form["c1"])
        # If c1=1, please input the following paramaters:
        if c1 == 1:
            d = float(request.form["d"])   # water depth (m)    
            X = request.form["X_1"]
            X = data_service.data_conv_int(X)            
            U = float(request.form["U_1"])  # wind speed (m/s)
            el = float(request.form["el_1"])   # the elevation of the wind speed (m)         
            gamma = float(request.form["gamma_1"])   # peakedness parameter for JONSWAP (between 1 and 7, but 3.30 is normally recommended)
            Hs = float(request.form["Hs_1"])   # significant wave height (m)
            Tz = float(request.form["Tz_1"])  # average zero-crossing period from data (s)
            Ts = request.form["Ts_1"] # significant wave period (s)
            Ts = data_service.data_conv(Ts)
            Tp = None

        # If c1=2, please input the following paramaters:
        if c1 == 2:
            X = request.form["X_2"]
            X = data_service.data_conv_int(X)   # fetch length (m)
            U = float(request.form["U_2"])   # wind speed m/s).             
            el = request.form["el_2"]  # the elevation of the wind speed (m). 
            el = data_service.data_conv(el)            
            gamma = float(request.form["gamma_2"])   # peakedness parameter in JONSWAP (between 1 and 7, but 3.30 is normally recommended). Optional
            Hs = float(request.form["Hs_2"])   # 5 # significant wave height (m)  
            Tz = request.form["Tz_2"]  # measured average zero-crossing period (s)
            Tz = data_service.data_conv(Tz)
            Ts = float(request.form["Ts_2"])   # measured significant period (s)
            Tp = request.form["Tp"]  # Tz: period of spectral peak (s)
            Tp = data_service.data_conv(Tp)
            d = None       

        img_stream, heading, data1, data1_heading, data2, data2_heading, content, ending = wes.wave(c1, d, X, U, el, gamma, Hs, Tz, Ts, Tp)
        # return render_template("wave.html", img_stream=img_stream, heading=heading, data1=data1, data1_heading1=data1_heading1, data1_heading2=data1_heading2, data2=data2, data2_heading1=data2_heading1, data2_heading2=data2_heading2, content=content, ending=ending )
        return render_template("wave.html", img_stream=img_stream, heading=heading, data1=data1, data1_heading=data1_heading, data2=data2, data2_heading=data2_heading, content=content, ending=ending )
        # return render_template("wave.html", d=d)
    else:
        return render_template("wave.html")

@app.route("/greenampt.html", methods=["POST", "GET"])
def greenampt():
    if request.method == "POST":
        # Effective Rainfall Generation   
        # Primary Inputs (required)
        # thetar = float(request.form["thetar"]) # Residual soil moisture content (It can be assumed to be zero, if no actual value is avaiulable.)
        thetai = float(request.form["thetai"] )# Initial soil moisture content
        thetas = float(request.form["thetas"] )# Soil moisture content at saturation (i.e. porosity)
        Psi = float(request.form["psi"]) # Suction head (m)
        K = float(request.form["k"]) # Saturated hydraulic conductivity (cm/h)
        tol = 0.00001
        toln= 0.00001
        dti= float(request.form["dti"]) #6 time interval in the analysis, normally that used in hyetograph (min)
        nin= int(request.form["nin"])# The number of time intervals to be considered in the anlysis
        iyesno = int(request.form["iyesno"]) # Whether to generate an effective hyetograph (0: No; 1: Yes)
        # test1 = request.form["thetar"]
        mingzi = request.form["mingzi"]
        test2 = request.form["thetai"]
        test3 = request.form["thetas"]
        test4 = request.form["psi"]
        test5 = request.form["k"]
        # test6 = request.form["tol"]
        test7 = request.form["dti"]
        test8 = request.form["nin"]
        test9 = None
        test10 = None
        yesono = request.form["iyesno"]
        yesorno = int(request.form["iyesno"])+1
        ss1=0#Special Scenario 1#20220313
        ss2=0#Special Scenario 2#20220313
        ss3=0#Special Scenario 2#20220313
        headings = []
        if iyesno == 1:
            test9 = request.form["dd"]
            test10 = request.form["i"]
            dd = float(request.form["dd"])# Depression depth used in generating an effective hyetograph (mm), which has to be zero when iyesno=0.
            result = request.form["i"] # Hyetograph (mm/h) (The first value covers the period between time 0 and time 0+dti.)
            res = result.split(",")
            i = list(map(float, res))
            if sum(i)==0:#20121226
                iyesno=0#20220310
                ss3=1 #Special Scenario 1#20220310 
            else:    
                if sum(i)*dti/60<dd:#20121226
                    iyesno=0#20220310
                    ss1=1 #Special Scenario 1#20220310 
                else:
                    #print('---Effective Rainfall Generated by Green-Ampt Infiltration Method---')
                    #print('Time Moment (minute)','  Intensity (mm/h)')
                    headings = [" 时刻 (minute) ","  雨强 (mm/h) "]
                    # heading1.append(headings_msg1)
                    # heading2.append(headings_msg2)
        if iyesno==0:
            i=[0 for k in range(nin)]# Hyetograph (mm/h) (The first value covers the period between time 0 and time 0+dti.)
            dd=0                
        # headings = ("时刻 (minutes)","雨强 (mm/h)")
        ending = "---结果展示结束---"
        plot_url, data, eff, note, note2 = wes.greenampt(thetai, thetas, Psi, K, dti, nin, dd, i, iyesno, ss1, ss2, ss3)
        # print("note is", note)
        # print("note2 is", note2)
        # print("yesono",yesono)
        # print("yesorno",yesorno)
        # print("mingzi is",mingzi)
        return render_template('greenampt.html',mingzi=mingzi,yesornot=yesorno, plot_url=plot_url,headings=headings,ending=ending,data=data,eff=eff,note=note,test2=test2,test3=test3,test4=test4,test5=test5,test7=test7,test8=test8,test9=test9,test10=test10,yesono=yesono,note2=note2)
    else:  
        return render_template("greenampt.html")

@app.route("/gumbel.html", methods=["POST", "GET"])
def gumbel():
    if request.method == "POST":
        pq = "物理量"
        unitx = "无单位"
        unitt = "单位时段"
        mingzi = request.form["mingzi"]
        pq_1 = request.form["pq"]
        if not pq_1:
            pq = pq
        elif not pq_1.strip():
            pq = pq
        else:
            pq = pq_1
        unitx_1 = request.form["unitx"]
        if not unitx_1:
            unitx = unitx
        elif not unitx_1.strip():
            unitx = unitx
        else:
            unitx = unitx_1
        unitt_1 = request.form["unitt"]
        if not unitt_1:
            unitt = unitt
        elif not unitt_1.strip():
            unitt = unitt
        else:
            unitt = unitt_1
        i1 = int(request.form["i1"])
        i2 = int(request.form["i2"])
        meanx,sdx,n = '','',''
        dataolist = ' '
        i3 = ' '
        if i2 == 1: 
            meanx = float(request.form["meanx"])
            sdx = float(request.form["sdx"])
            n = int(request.form["n"])
        if i2 == 2:
            dataolist = request.form["datao"]
            i3 = int(request.form["i3"])
        # print('pq is',pq)
        # print('unitx is',unitx)
        # print('unitt is',unitt)
        # print('i1 is',i1)
        # print('i2 is',i2)
        # print('i3 is',i3)
        # print('meanx is',meanx)
        # print('sdx is',sdx)
        # print('n is',n)
        # print('dataolist is',dataolist)
        plot_url, nCl2, nlen, note1, note2, note3, data3, note4, data4, note5, data5, data6, heading1, heading2, ending = wes.gumbel(pq, unitt, unitx, i1, i2, i3, meanx, sdx, n, dataolist)
        # print('nlen is',nlen)
        # data6 = list(data6)
        # print(data5)
        # print(data6)
        return render_template("gumbel.html", nCl2=nCl2, nlen=nlen, mingzi=mingzi, pq=pq, unitx=unitx, unitt=unitt, i1=i1, i2=i2, i3=i3, meanx=meanx, sdx=sdx, n=n, dataolist=dataolist, plot_url=plot_url, note1=note1, note2=note2, note3=note3, data3=data3, note4=note4, data4=data4, note5=note5, data5=data5, data6=data6, heading1=heading1, heading2=heading2, ending=ending)
    else:
        return render_template("gumbel.html")

if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
