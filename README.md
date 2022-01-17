# CongVRP
Dưới đây sẽ hướng dẫn cách dùng package này từ A đến Z để lập lộ trình tối ưu cho các phương tiện với các ràng buộc.

## Import package
Sau đây sẽ là cách import các lớp cần thiết 

```python
from CongVRP import CongVRP
from CongVRP import Cluster, City
```

## Khởi tạo City
Một lớp City sẽ tương ứng với một điểm trên bản đồ. Lớp City khi khởi tạo cần định nghĩa các tham số:

- Số thực x : tọa độ X
- Số thực y : tọa độ Y
- Số nguyên ID : ID gán cho điểm đó

Ví dụ:
```python
newCity = City(x = 100, y = 100, id = 9)
```


## Khởi tạo Cluster
Đầu tiên, mình khởi tạo một Cluster chứa các City là các điểm trên bản đồ. Và để thêm City vào Cluster, mình dùng hàm Cluster.append(City), cụ thể làm như sau:
```python
cluster = Cluster()
newCity = City(x = 100, y = 100, id = 9)
cluster.append(City(x=coordinate[i].x, y=tmp[i].coordinate[i].y, id = i))
```

