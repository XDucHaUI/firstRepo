b = 12
# kiểu dữ liệu của biến bất kỳ nào đó
print(type(b))


# Lấy toàn bộ nội dung thư viện decimal ( Bắt buộc để mở thư viện Deciaml)
from decimal import*
# Lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 30
d = Decimal(10)/Decimal(3) # Decimal phân biệt hoa và thường ( Nên Viết Hoa)
print (d)


# Tạo phân số thì sử dụng hàm fractions( Ví dụ 6 chia 9)
# Bắt buộc phải khai báo thư viện bằng cách import thư viện
#frac = fractions(6,9)
#print(type(frac))

# Tạo số thực thì sử dụng hàm complex
c = complex(2,5)
print(c)
