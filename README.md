# CongVRP
Dưới đây sẽ hướng dẫn cách dùng lib này từ A đến Z để lập lộ trình tối ưu cho các phương tiện. Lib này được viết hoàn toàn bằng python 3.

## Cài đặt các package 

Các tên của các package python được liệt kê trong `requirements.txt`.
Để cài đặt dùng lệnh sau trên CLI.

```
pip3 install -r requirements.txt
```

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
- Số nguyên ID : Index gán cho điểm đó

Ví dụ:
```python
newCity = City(x = 100, y = 100, id = 9)
```


## Khởi tạo Cluster
Đầu tiên, mình khởi tạo một Cluster chứa các City là các điểm trên bản đồ. Và để thêm City vào Cluster, mình dùng hàm Cluster.append(City), cụ thể làm như sau:
```python
cluster = Cluster()
newCity = City(x = 100, y = 100, id = 9)
cluster.append(newCity)
```

## Khởi tạo lớp chính 
Để khởi tạo lớp chính là CongVRP, làm như sau:
```python
CongVRP = CongVRP()
```

## Định nghĩa hàm khoảng cách
Để định nghĩa hàm khoảng cách giữa 2 điểm trên bản đồ, tạo hàm nhận vào là 2 đối tượng City và trả về khoảng cách giữa 2 đối tượng đó là số thực hoặc số nguyên.

Sau khi định nghĩa hàm thì mình đăng kí vào lớp chính CongVRP cụ thể như sau:

Ví dụ:
```python
def distance_callback(cityA, cityB):
    xDis = abs(cityA.x - cityB.x)
    yDis = abs(cityA.y - cityB.y)
    distance = xDis + yDis

    return distance
    
CongVRP.RegisterTransitCallback(distance_callback)
```

## Thêm ràng buộc Pickup and Delivery
Để thêm yêu cầu về Pickup and Delivery, gọi hàm CongVRP.AddPickupAndDelivery với đầu vào là 2 số nguyên chỉ index của điểm pickup và điểm delivery. Cụ thể ví dụ như sau:

```python
CongVRP.AddPickupAndDelivery(pickup_index, delivery_index)
```

## Lập lộ trình

Đây là bước lập lộ trình, mình sẽ gọi hàm find_route ở lớp CongVRP với các đầu vào như sau:

- Cluster: đối tượng Cluster chứa dữ liệu của các đối tượng City
- start: index của điểm xuất phát
- end: index của điểm kết thúc
- n_cluster: (Mặc định 15) Số lượng tối đa của điểm trong mỗi Cluster

Và hàm sẽ trả về một lộ trình dưới dạng list chứa các đối tượng City theo thứ tự lớn dần.

Để ý là n_clusters là số lượng thành phần tối đa của một cụm mỗi khi phân cụm. Số này để càng thấp thì chương trình chạy càng nhanh nhưng độ tối ưu sẽ giảm và ngược lại. Số tối ưu cho kết quả tối ưu cân đối với thời gian chạy sẽ được đặt mặc định là 15.

Sau đây là code ví dụ:

```python
path = CongVRP.find_route(cluster, IndexDepartment, IndexDestination, n_clusters = 15)
```

## Phân lịch cho nhiều phương tiện

Để phân lịch cho nhiều hơn 1 phương tiện, dùng hàm CongVRP.MultipleVehicles với đầu vào là: 

- path: lộ trình sau khi tìm được dưới dạng list của các lớp City
- num_vehicles: Số lượng phương tiện

Đầu ra trả về một list chứa các list là lộ trình của mỗi phương tiện.

Code ví dụ:
```python
path = CongVRP.MultipleVehicles(path, 4)
```


