import math
i=0
for i in range(90):
    i=i+1
    de_i=math.radians(i)
    m_sin=math.sin(de_i)
    m_cos=math.cos(de_i)
    m_tan=math.tan(de_i)
    if i==90:
        m_tan="값이 존재하지 않습니다.(무한대)"
        print(f"sin{i}: {m_sin:.4f} == cos{i}: {m_cos:.4f} == tan{i}: {m_tan}") 
    else:
        print(f"sin{i}: {m_sin:.4f} == cos{i}: {m_cos:.4f} == tan{i}: {m_tan:.4f}")         #소수점 4자리까지 출력