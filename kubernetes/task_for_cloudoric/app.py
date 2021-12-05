from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/hello')
def hello():    
    count = redis.incr('hits')                
    redis.set("msg:hello", "  deepak:-> ")
    msg = redis.get("msg:hello")
    return 'Hello  {} : {} .\n'.format(msg,count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
