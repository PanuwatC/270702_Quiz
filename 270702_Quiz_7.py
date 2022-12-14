import numpy as np                                          ## import library numpy as np
M = np.arange(12.0).reshape((4, 3)) + 1                     ## กำหนดขนาดเมตริกซ์ 4*3 และเพิ่มค่าในเมตริกซ์ 12 ค่าเริ่มจาก 0 ถึง 11 จากนั้น เพิ่มทุกค่าในเมตริกซ์ขึ้นอีก 1
print(M[2,:])                   # [7. 8. 9.]                ## แสดงทุกค่าในเมตริกซ์ ที่แถวเท่ากับ 2

print(M[2:])                    # [[ 7.  8.  9.]            ## แสดงทุกค่าในเมตริกซ์ ที่แถวเท่ากับ 2 เป็นต้นไป
                                #  [10. 11. 12.]]
