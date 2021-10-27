class Doctor_proto:
    def __init__(self, x):
        self.x = x
x = Doctor_proto(5)
x.q = 8
y = Doctor_proto(7)
print(y.q)