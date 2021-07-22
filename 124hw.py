from flask import Flask, json,jsonify,request

app = Flask(__name__)

contacts = [
    {
        'id':1,
        'name':U'Shreya',
        'number':U'8765465787',
        'done':False
    },
     {
        'id':1,
        'name':U'Lily',
        'number':U'9928734123',
        'done':False
    }
]

@app.route('/get-data')

def getcontacts():
    return jsonify({
        'data':contacts
    })


@app.route('/add-data',methods=['POST'])
def addcontacts():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data to add to your contacts'
        },400
        )

    contacts2 = {
          
        'id':contacts[-1]['id']+1,
        'name':request.json['name'],
        'number':request.json.get('number',''),
        'done':False

    }

    contacts.append(contacts2)

    return jsonify({
        'status':'success',
        'message':'contact added successfully'
    })


if __name__ == '__main__':
    app.run()
