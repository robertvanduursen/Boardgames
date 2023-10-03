"""

Notes and experiment file for ripping Sprites out of KoF 13

"""

infoPages = [
    r"https://graphics.stanford.edu/~mdfisher/D3D9Interceptor.html",
    r"https://renderdoc.org/docs/getting_started/faq.html",
]

history = '''

Renderdoc does not support D3D9 (Direct3D 9), so Renderdoc is not an option

an successful attempt to use the Global Hook method yielded the use of D3D9 as the display driver DLL  

'''


def current_plan():
    """ current thing to do """

    info = r"# https://graphics.stanford.edu/~mdfisher/D3D9Interceptor.html"

    idea = '''
        this approach relies on putting a proxy in place for the DirectX .DLL 
        - similar to the USB Sniffer
        
        the framework of the interceptor may provide the needed services
    
    '''

    return 'continue with D3D9Interceptor'
