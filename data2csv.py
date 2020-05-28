import cv2 
import os 
import json
import csv



def data_damp(jsn_name,writer,i):
    jsn=open(jsn_name,'r')
    jsn=json.load(jsn)
    seq=jsn["sequence"]
    f_len=len(seq)
    for f in range(f_len):
        f_name="../dataset/signate/images/train/train_{0:02d}/img1/{0:04d}.jpg".format(i,f)
        for key in seq[f].keys():
            label=seq[f][key]
            for n in label:
                data=list()
                box=n["box2d"]
                x1,y1,x2,y2=box[0],box[1],box[2],box[3]
                box=str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)
                #c=str(class_key[key])
                data.append([f_name]+[x1]+[y1]+[x2]+[y2]+[key])
                writer.writerow(data[0])
        #if f>=2:
         #   break




if __name__ == "__main__":
    #m_dir="train_videos"
    train_num=1
    val_num=[23,24]
    class_key={"Signal":0,"Signs":1,"Pedestrian":2,"Car":3,"Motorbike":4,\
        "Bicycle":5,"Truck":6,"Svehicle":7,"Bus":8,"Track":9}
    for key in class_key.keys():
        with open ("class.csv",mode="a") as t: 
            writer=csv.writer(t)
            writer.writerow([key]+[class_key[key]])
    
    for i in range(train_num):
        dri_name="train_{0:02d}".format(i)
        jsn_name=dri_name+".json"
        #jsn_name=os.path.join("train_annotations",jsn_name)

        txt_path="train.csv"
        with open(txt_path,mode="a") as t:
            writer=csv.writer(t)
            data_damp(jsn_name,writer,i)
    """
    for i in val_num:
        dri_name="train_{0:02d}".format(i)
        jsn_name=dri_name+".json"
        jsn_name=os.path.join("train_annotations",jsn_name)

        txt_path="val.csv"
        with open(txt_path,mode="a") as t:
            writer=csv.writer(t)
            data_damp(jsn_name,writer,i)
    """

        
