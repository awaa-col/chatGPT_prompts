from flask import request, Flask
server = Flask(__name__)
server.route('/', methods=["POST"])
def get_message():
    message_json=request.json#监听到的json
    message_type=message_json['message_type']#获取到的消息类型(str)
    qq_number=message_json['user_id']#发送者的QQ号(int)
    message=message_json['raw_message']#获取到的消息(str)
    cq_data=process_cq_code(message)#处理后的CQ码内的内容
    print(message_json) 
    return qq_number

if __name__ == '__main__': 
    server.run(port=5480, host='0.0.0.0', use_reloader=False,debug=True)
