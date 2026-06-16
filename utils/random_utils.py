import random as rd
import string as st

def generate_assignment_code():
    chars = st.ascii_uppercase + st.digits
    suffix = ''.join(rd.choices(chars, k=4))
    return f"PY-{suffix}"