import huaweisms.api.user
import huaweisms.api.wlan
import huaweisms.api.sms


class smsController:
    def __init__(self):
        pass
    
    def testConn(self):
        ctx = huaweisms.api.user.quick_login("admin", "admin")
        print(ctx)
        print(type(ctx))
        return str(ctx.api_base_url)   

    def emptyOutbox(self):
        ctx = huaweisms.api.user.quick_login("admin", "admin")
        res = huaweisms.api.sms.get_sms(ctx,box_type=2,qty=5)
        smsMessages = res['response']
        outboxList = smsMessages['Messages']['Message']
        for sms in outboxList:
            index = sms['Index']
            delete = huaweisms.api.sms.delete_sms(ctx,index)



    
    def send_sms(self,req_data):
        dest = req_data['number']
        msg = req_data['message']

        ctx = huaweisms.api.user.quick_login("admin", "admin")
        res = huaweisms.api.sms.send_sms(
            ctx,
            dest,
            msg
        )
        self.emptyOutbox()
        return [{
            "return_status":"success",
            "return_message":res
        }]
    
    def read_sms(self,req_data):
        qty = req_data['qty']
        if(int(qty) > 50):
            return [{
                "return_status":"failed",
                "return_message":"quanty get sms must be less or equal than 50"
            }]
        else:
            ctx = huaweisms.api.user.quick_login("admin", "admin")
            res = huaweisms.api.sms.get_sms(ctx,qty=50)
            smsMessages = res['response']
            if(int(smsMessages['Count']) == 0):
                return [{
                    "return_status":"success",
                    "return_message":"there are no inbox"
                }]
            else:
                return [{
                    "return_status":"success",
                    "return_message":smsMessages['Messages']['Message']
                }]
        
    def delete_sms(self,req_data):
        index = req_data['index']

        ctx = huaweisms.api.user.quick_login("admin", "admin")
        res = huaweisms.api.sms.delete_sms(ctx,index)
        return [{
            "return_status":"success",
            "return_message":res
        }]
    
    def rebootDevice(self):
        try:
            ctx = huaweisms.api.user.quick_login("admin", "admin")
            res = huaweisms.api.sms.reboot(ctx)
            return [{
                    "return_status":"success",
                    "return_message":"there are no inbox"
                }] 
        except Exception as e:
            return [{
                "return_status":"failed",
                "return_message":str(e)
            }]
    
