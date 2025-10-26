
import numpy as np
from sklearn import linear_model

# Dữ liệu chiều cao (cm)
X = np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T
# Dữ liệu cân nặng (kg)
y = np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])

# Xây dựng Xbar = [1, X]
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

# Tính toán nghiệm theo công thức hồi quy tuyến tính
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)

# Huấn luyện bằng thư viện scikit-learn
regr = linear_model.LinearRegression()
regr.fit(X, y)

# So sánh kết quả
print("scikit-learn's solution: w_1 = %.4f, w_0 = %.4f" % (regr.coef_[0], regr.intercept_))
print("Our solution           : w_1 = %.4f, w_0 = %.4f" % (w[1], w[0]))

# Dự đoán cân nặng
yourHeight = float(input("Nhập chiều cao của bạn (cm): "))
yourWeight = regr.coef_[0] * yourHeight + regr.intercept_
print("Chiều cao của bạn là %.1f cm, tôi dự đoán cân nặng của bạn là %.2f kg" % (yourHeight, yourWeight))
