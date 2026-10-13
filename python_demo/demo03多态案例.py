from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class OrderItem:
    name: str
    price: float
    quantity: int

    @property
    def total_price(self):
        return self.price * self.quantity


class DiscountStrategy(ABC):
    """折扣策略抽象类"""

    @abstractmethod
    def calculate(self, amount: float) -> float:
        """返回折扣后的价格"""
        pass


class NoDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount


class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount: float):
        self.discount = discount

    def calculate(self, amount: float) -> float:
        return amount * self.discount


class FullReductionDiscount(DiscountStrategy):
    def __init__(self, threshold: float, reduction: float):
        self.threshold = threshold
        self.reduction = reduction

    def calculate(self, amount: float) -> float:
        if amount >= self.threshold:
            return amount - self.reduction
        return amount


class PaymentMethod(ABC):
    """支付方式抽象类"""

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class Alipay(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"使用支付宝支付 ¥{amount:.2f}")
        return True


class WechatPay(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"使用微信支付 ¥{amount:.2f}")
        return True


class BankCard(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"使用银行卡支付 ¥{amount:.2f}")
        return True


class Order:
    def __init__(
        self,
        order_id: str,
        items: list[OrderItem],
        discount: DiscountStrategy,
        payment: PaymentMethod,
    ):
        self.order_id = order_id
        self.items = items
        self.discount = discount
        self.payment = payment

    def calculate_total(self) -> float:
        original_price = sum(item.total_price for item in self.items)
        return self.discount.calculate(original_price)

    def checkout(self):
        original_price = sum(item.total_price for item in self.items)
        final_price = self.calculate_total()

        print(f"\n订单号：{self.order_id}")
        print(f"商品原价：¥{original_price:.2f}")
        print(f"优惠后价格：¥{final_price:.2f}")

        if self.payment.pay(final_price):
            print("支付成功")
        else:
            print("支付失败")


def main():
    items = [
        OrderItem("Python 入门", 59.9, 1),
        OrderItem("Python 进阶", 89.9, 2),
    ]

    orders = [
        Order(
            "ORDER001",
            items,
            PercentageDiscount(0.8),
            Alipay(),
        ),
        Order(
            "ORDER002",
            items,
            FullReductionDiscount(200, 30),
            WechatPay(),
        ),
        Order(
            "ORDER003",
            items,
            NoDiscount(),
            BankCard(),
        ),
    ]

    for order in orders:
        order.checkout()


if __name__ == "__main__":
    main()