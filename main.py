from flask import Flask, render_template, Response,request,jsonify

from core import VideoCamera
import cv2
import pymysql
import time
from Data_Access import testdb

from variables import static_variables

import webbrowser

app = Flask(__name__)



@app.route('/test/<num>')
def test(num):

    return render_template('test.html',num=num)


class static_tracker:
    trackers_list=[]
    tracker_queues_list = []
    fname=""
    ttt = []
    restricted = []
    counter=0

@app.route('/play')
def play():
    static_variables.paused=False
    return "hfg"

@app.route('/pause')
def pause():
    static_variables.paused=True
    return "hfg"
@app.route('/snap')
def snap():
    static_variables.snap=True
    return "hfg"

@app.route('/background_process_test')
def background_process_test():
    static_variables.pressed=True
    return "hfg"

@app.route('/')
def index():
    static_variables.fname = ""
    static_variables.Frame_count = 0
    static_variables.trackers_list = []
    static_variables.tracker_queues_list = []
    static_variables.restricted = []
    static_variables.lost_trackers = []
    static_variables.lost_detections = []
    static_variables.entrance_information = []
    static_variables.op = True
    static_variables.info_set=[]
    #testdb.clear_tables()

    return render_template('Home.html')
@app.route('/video',methods=['GET','POST'])
def open_video():

    if request.method == 'POST':
        f = request.files['file']
        static_tracker.fname="Sample_Videos/"+f.filename

    return render_template('video.html')
testss="blazzzzzzzz"


@app.route('/game')
def live_game():


   results = testdb.getdata()
   return str(results)



@app.route('/analytics')
def analytics():
    framelist = []
    countlist = []
    r_frames = []
    r1 = []
    r2 = []
    r3 = []
    all_info=[]
    s_array = []

    for itm in testdb.get_session_list():
        s_array.append(itm)
    for raw in testdb.getcounts():
        framelist.append(raw[0])
        countlist.append(raw[1])
    for raw1 in testdb.get_region_counts():
        r_frames.append(raw1[0])
        r1.append(raw1[1])
        r2.append(raw1[2])
        r3.append(raw1[3])
    for info in testdb.getdata():
        inner=[]
        for i in info:
            inner.append(i)
        all_info.append(inner)


    test=["sasa","ascas","sdgs","df"]
    try:
        r1_mean = (sum(r1) * 1.0) / len(r1)
        r2_mean = (sum(r2) * 1.0) / len(r2)
        r3_mean = (sum(r3) * 1.0) / len(r3)
    except ZeroDivisionError:
        r1_mean =0
        r2_mean =0
        r3_mean =0

    entrance_info = testdb.get_enterance_info()
    labels = ["Region 1", "Region 2", "Region 3"]
    pie_val = [r1_mean, r2_mean, r3_mean]
    colors = ["#F7464A", "#46BFBD", "#FDB45C"]
    frame_count=testdb.get_frame_num()
    s_num = testdb.get_session_num()
    pop_mean = testdb.get_mean_pop()
    r_count = len(static_variables.restricted)



    return render_template('dashboard.html', values=countlist, s_array=s_array, labels=framelist, r_frames=r_frames, r1=r1, r2=r2, r3=r3,
                           results=entrance_info, pie_val=pie_val, all_info=all_info, frame_count=frame_count, s_num=s_num, popl_mean=pop_mean, r_count=r_count)


@app.route('/analytics/<session_number>')
def analyticsn(session_number):
    framelist = []
    countlist = []
    r_frames = []
    r1 = []
    r2 = []
    r3 = []
    all_info=[]
    s_array = []

    for itm in testdb.get_session_list():
        s_array.append(itm)
    for raw in testdb.getcounts(session_number):
        framelist.append(raw[0])
        countlist.append(raw[1])
    for raw1 in testdb.get_region_counts(session_number):
        r_frames.append(raw1[0])
        r1.append(raw1[1])
        r2.append(raw1[2])
        r3.append(raw1[3])
    for info in testdb.getdata(session_number):
        inner=[]
        for i in info:
            inner.append(i)
        all_info.append(inner)


    test=["sasa","ascas","sdgs","df"]
    try:
        r1_mean = (sum(r1) * 1.0) / len(r1)
        r2_mean = (sum(r2) * 1.0) / len(r2)
        r3_mean = (sum(r3) * 1.0) / len(r3)
    except ZeroDivisionError:
        r1_mean =0
        r2_mean =0
        r3_mean =0

    entrance_info = testdb.get_enterance_info(session_number)
    labels = ["Region 1", "Region 2", "Region 3"]
    pie_val = [r1_mean, r2_mean, r3_mean]
    colors = ["#F7464A", "#46BFBD", "#FDB45C"]
    frame_count=testdb.get_frame_num(session_number)
    s_num = testdb.get_session_num()
    pop_mean = testdb.get_mean_pop(session_number)
    r_count = len(static_variables.restricted)



    return render_template('dashboard.html', values=countlist, s_array=s_array, labels=framelist, r_frames=r_frames, r1=r1, r2=r2, r3=r3,
                           results=entrance_info, session_number=session_number, pie_val=pie_val, all_info=all_info, frame_count=frame_count, s_num=s_num, popl_mean=pop_mean, r_count=r_count)





@app.route('/camera',methods=['GET','POST'])
def open_cam():

    return render_template('camera.html')


def gen(camtest):
    while True:
        try:
            if (static_variables.paused):
                continue

            frame = camtest.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        except :
            print (Exception)
            cv2.destroyAllWindows()
            break


@app.route("/myStatus")
def getStatus():
    results = "das"

    return results

@app.route('/video_feed')
def video_feed():
    static_variables.fname = ""
    static_variables.Frame_count = 0
    static_variables.trackers_list = []
    static_variables.tracker_queues_list = []
    static_variables.restricted = []
    static_variables.lost_trackers = []
    static_variables.lost_detections = []
    static_variables.op = True
    static_variables.entrance_information = []
    static_variables.info_set = []
    static_variables.camera_input = False
    static_variables.session_number=testdb.get_session_num()+1


    return Response(gen(VideoCamera(static_tracker.fname)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cam_feed')
def cam_feed():
    static_variables.fname = ""
    static_variables.Frame_count = 0
    static_variables.trackers_list = []
    static_variables.tracker_queues_list = []
    static_variables.restricted = []
    static_variables.lost_trackers = []
    static_variables.lost_detections = []
    static_variables.op = True
    static_variables.entrance_information = []
    static_variables.info_set = []
    static_variables.camera_input=True
    static_variables.session_number = testdb.get_session_num() + 1
    return Response(gen(VideoCamera(0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'
    webbrowser.open_new(url)
    app.run(host='localhost', debug=False ,threaded=True)
