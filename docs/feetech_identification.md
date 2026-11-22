$\theta_d^f$ : ファームウェア単位での要求角度 $\theta$

$\epsilon = \theta_d^f - \theta^f$

### ファームウェア単位での誤差

> $\lambda$ はデューティ比、すなわち **PWM**

$\epsilon^f = \epsilon \frac{4096}{2\pi}$

> 12 bit

### ファームウェアのデューティ比


$\lambda^f = K_p \epsilon^f$

$\lambda = K_p K_g\epsilon$


$R = 2.5\Omega$

------

$\lambda = \epsilon K_p K_g$

$K_g = \frac{\lambda}{\epsilon K_p }$
