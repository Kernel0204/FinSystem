from django.db import models
import datetime

# Create your models here.
class users(models.Model):
    """ユーザの基本情報を定義するテーブル"""
    first_name = models.CharField(max_length=255 ,null=False)
    last_name = models.CharField(max_length=255 ,null=False)
    first_name_ruby = models.CharField(max_length=255 ,null=False)
    last_name_ruby = models.CharField(max_length=255 ,null=False)
    email = models.EmailField(max_length=75 ,null=False)
    thumbnail_path = models.CharField(max_length=255)
    birthday = models.DateField(null=False)
    sex = models.ForeignKey("sexs" , related_name="sex_id")
    groups = models.ForeignKey("groups", related_name="group_id")
    position = models.CharField(max_length=255 ,null=False)
    phone_number = models.CharField(max_length=255 ,null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return u'%s' % (str(self.first_name) + str(self.last_name))


class groups(models.Model):
    """ユーザが属するグループを定義するテーブル"""
    COMPANY_OR_NOT = (
        (1, u'個人事業主'),
        (2, u'株式会社'),
        (3, u'合同会社')
    )
    name = models.CharField(max_length=255, null=False)
    company_or_ind = models.IntegerField()  # 法人か個人か
    thumbnail_path = models.CharField(max_length=255)
    email = models.EmailField(max_length=75, null=False)
    post_num = models.CharField(max_length=255, null=False)
    prefecture = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    address1 = models.CharField(max_length=255, null=False)
    address2 = models.CharField(max_length=255)
    member_type = models.ForeignKey("membertype", related_name="member_type")
    job_type = models.ForeignKey("jobtypes", related_name="job_type")
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return u'%s' % (self.name)


class jobtypes(models.Model):
    """職業タイプを定義するテーブル"""
    name = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return u'%s' % (self.name)


class sexs(models.Model):
    """性別を定義するテーブル"""

    name = models.CharField(max_length=255 ,null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return u'%s' % (self.name)


class membertype(models.Model):
    """会員ステータスを定義するテーブル"""
    name = models.CharField(max_length=255 ,null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return u'%s' % (self.name)

class fluctationincome(models.Model):
    """変動収益を定義するテーブル"""
    user = models.ForeignKey("users" ,related_name="user_fluctationincome")
    name = models.CharField(max_length=255 ,null=False)
    amount = models.IntegerField()
    paidornot = models.ForeignKey("paidstatuse", related_name="paidornot_fluctationincome") #入金してくれたかどうか
    income_category = models.ForeignKey("incomecategory" ,related_name="income_category_fluctationincome")
    date = models.DateField() #入金日
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)


class staticincome(models.Model):
    """固定収入の基本情報を定義するテーブル"""
    user = models.ForeignKey("users", related_name="user_staticincome")
    name = models.CharField(max_length=255, null=False)
    amount = models.IntegerField()
    income_category = models.ForeignKey("incomecategory", related_name="income_category_staticincome")
    date = models.DateField()  # 入金日
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)



class staticincomedetail(models.Model):
    """固定収入を記録するテーブル"""
    name = models.CharField(max_length=255 ,null=False)
    amount = models.IntegerField()
    paidornot = models.ForeignKey("paidstatuse", related_name="paidornot_staticincomedetail")  # 入金してくれたかどうか
    paid_date = models.DateTimeField()
    delay_or_not = models.ForeignKey("delayornot",related_name="delay_or_not_staticincomedetail") #デフォルトは延滞無し
    delay_amount = models.IntegerField() #延滞料
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)



class fluctationexpense(models.Model):
    """変動コストを定義するテーブル"""
    user = models.ForeignKey("users", related_name="user_3")
    name = models.CharField(max_length=255, null=False)
    amount = models.IntegerField()
    income_category = models.ForeignKey("incomecategory", related_name="income_category_fluctationexpense")
    date = models.DateField()  # 入金日
    paidornot = models.ForeignKey("paidstatuse", related_name="paidornot_fluctationexpense")
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)


class staticexpense(models.Model):
    """固定費の基本情報を定義するテーブル"""
    user = models.ForeignKey("users", related_name="user_4")
    name = models.CharField(max_length=255, null=False)
    amount = models.IntegerField()
    income_category = models.ForeignKey("incomecategory", related_name="income_category_staticexpense")
    date = models.DateField()  # 入金日
    paidornot = models.ForeignKey("paidstatuse", related_name="paidornot_staticexpense")
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)


class staticexpensedetail(models.Model):
    """固定収入を記録するテーブル"""
    name = models.CharField(max_length=255, null=False)
    amount = models.IntegerField()
    paidornot = models.ForeignKey("paidstatuse", related_name="paidornot_staticexpensedetail")  # 入金したかどうか
    paid_date = models.DateTimeField()
    delay_or_not = models.ForeignKey("delayornot", related_name="delay_or_not_staticexpensedetail")  # デフォルトは延滞無し
    delay_amount = models.IntegerField()  # 延滞料
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)



class debt(models.Model):
    """借入基本情報を定義するテーブル
    記録は、固定費の部分に登録すること
    """
    name = models.CharField(max_length=255, null=False)
    user = models.ForeignKey("users", related_name="user_debt")
    lender_name = models.CharField(max_length=255, null=False)
    repayment_day = models.DateField() #最終的な返済日
    repayment_num = models.IntegerField(null=False) #分割階数
    amount = models.IntegerField(null=False) #借入総額
    balance = models.IntegerField(null=False) #残高
    interest_rate = models.FloatField(null=False) #利子
    repayment_interval = models.IntegerField(null=False) #返済間隔
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)



class incomecategory(models.Model):
    """収益の種類を定義するテーブル"""
    name = models.CharField(max_length=255,null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)


class expensecategory(models.Model):
    """支出の種類を定義するテーブル"""
    name = models.CharField(max_length=255,null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)


class paidstatuse(models.Model):
    """支払いステータスを定義するテーブル"""
    name = models.CharField(max_length=255 ,null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)

class delayornot(models.Model):
    """支払いに滞納があったかどうかの状態を定義するテーブル"""
    name = models.CharField(max_length=255 ,null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(default=datetime.datetime.now)