from flask import Flask, redirect, url_for, render_template, request, jsonify
import random

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def game(gues_num, original_num):
    true_num = 0
    true_loc = 0
    #for i in set([int(i) for i in gues_num]):
    #    true_num += original_num.count(str(i))
    temp = list(original_num)[::]
    for i in gues_num:
        for index, j in enumerate( temp):
            if i == j: 
                true_num +=1
                del temp[index]
                break

    for i in zip(gues_num, original_num):
        if i[0] == i[1]: true_loc += 1
    
    return {"true_num":true_num, "true_loc":true_loc, "gues_num":gues_num}

@app.route("/")
def home():
    if request.is_json:
        if int(request.args.get("game")) == 1 :
            gues_num = str(request.args.get("guess"))
            original_num = str(request.args.get("original_number"))
            if len(gues_num) > 50 or len(original_num) > 50 or len(gues_num) == 0: return 204 

            result = game(gues_num, original_num)
            return jsonify(result)
        else:
            range_rand = int(request.args.get("range_rand"))
            if range_rand > 50: return 204 
            
            rand = random.randint(10**(range_rand-1),10**range_rand-1)
            return (jsonify({"rand":f"{rand}"}),200)
    return render_template("index.html")




