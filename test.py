try:
    i = 1/0
except Exception as e:
    print(f'ERROR:\n\tTYPE   : {type(e).__name__}\n\tMESSAGE: {e.args}')