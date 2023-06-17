import random
import gptInput

add_message = ""
mode = ''

def handle_response(message) -> str:
    p_message = message.lower()
    global add_message
    global mode 

    if p_message == '!fear':
        add_message = "use a fearful voice and tone"
        mode = 'Fear'
        return "'Fear mode is activated!'"
    
    if p_message == '!humor':
        add_message = "use a humor voice and tone"
        mode = 'Humorous'
        return "'Humorous mode is activated!'"
    
    if p_message == '!tired':
        add_message = "use a tired voice and tone"
        mode = 'Tired'
        return "'Tired mode is activated!'"
    
    if p_message == '!sassy':
        add_message = "use a sassy voice and tone"
        mode = 'Sassy'
        return "'Sassy mode is activated!'"

    if p_message == '!stop':
        add_message = ""
        mode = ''
        return "'Mode is turned off'"
    
    if p_message == '!mode':
        if len(mode) == 0:
            return "'Mode is currently turned off'"
        else:
            return mode + " mode is currently activated"
    
    if p_message == '!help':
        return '''Keyword : Description\n
        !fear : Fearful mode\n
        !humor : Humorous mode\n
        !tired : Tired mode\n
        !sassy : Sassy mode\n
        !stop : Turn off the mode\n
        !mode : Show which mode is turned on'''

    f_message = p_message + " " + add_message
    reply = gptInput.gptReply(f_message)
    return reply
