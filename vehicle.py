class V:

    def __init__(self, m_s, m, h):

        self.m_s = m_s
        self.m = m
        self.a = h


modelX = V(240, 18, 100)

print("Model Max speed:",modelX.m_s)
print("Model Mileage:",modelX.m)
print("Model health:",modelX.a)