# Generated by Django 3.1 on 2020-08-27 05:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='收款金额')),
            ],
            options={
                'verbose_name': '账单',
                'verbose_name_plural': '账单',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wechat_id', models.CharField(blank=True, max_length=40, null=True, verbose_name='微信号')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='请输入正确的11位手机号', regex='^[0-9]{11}$')], verbose_name='手机号')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=2, null=True)),
                ('credit', models.IntegerField(default=0, verbose_name='积分')),
            ],
            options={
                'verbose_name': '顾客',
                'verbose_name_plural': '顾客',
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True, verbose_name='会员卡号')),
                ('discount', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='折扣')),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='余额')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='reception.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Maid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='请输入正确的身份证号，包含数字和大写X', regex='^[0-9]{17}[0-9X]$')], verbose_name='身份证号')),
                ('name', models.CharField(max_length=5, verbose_name='姓名')),
                ('cos_name', models.CharField(max_length=5, unique=True, verbose_name='昵称')),
                ('wechat_id', models.CharField(max_length=40, unique=True, verbose_name='微信号')),
                ('phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='请输入正确的11位手机号', regex='^[0-9]{11}$')], verbose_name='手机号')),
                ('available', models.BooleanField(default=False, verbose_name='空闲')),
                ('active', models.BooleanField(verbose_name='在职')),
                ('fulltime', models.BooleanField(verbose_name='全职')),
                ('price', models.PositiveSmallIntegerField(default=90, verbose_name='价格')),
            ],
            options={
                'verbose_name': '女仆',
                'verbose_name_plural': '女仆',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20, unique=True, verbose_name='项目')),
                ('price', models.PositiveSmallIntegerField(verbose_name='单价')),
                ('active', models.BooleanField(verbose_name='仍在提供')),
            ],
            options={
                'verbose_name': '价目表',
                'verbose_name_plural': '价目表',
                'ordering': ['item'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='名称')),
                ('price', models.PositiveSmallIntegerField(verbose_name='每小时价格')),
                ('available', models.BooleanField(default=True, verbose_name='空闲')),
            ],
            options={
                'verbose_name': '场地',
                'verbose_name_plural': '场地',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Serves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('active', models.BooleanField(default=True, verbose_name='进行中')),
            ],
            options={
                'verbose_name': '服务',
                'verbose_name_plural': '服务',
            },
        ),
        migrations.CreateModel(
            name='VoucherType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='名称')),
                ('note', models.CharField(max_length=200, verbose_name='使用条件')),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='实际收入')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='抵扣金额')),
            ],
            options={
                'verbose_name': '代金劵种类',
                'verbose_name_plural': '代金劵种类',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used', models.BooleanField(default=False, verbose_name='已使用')),
                ('meituan', models.BooleanField(default=False, verbose_name='美团/大众')),
                ('swift_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='流水号')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reception.customer')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.vouchertype')),
            ],
            options={
                'verbose_name': '代金券',
                'verbose_name_plural': '代金券',
                'unique_together': {('meituan', 'swift_number')},
            },
        ),
        migrations.CreateModel(
            name='ServesPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('price', models.PositiveSmallIntegerField(verbose_name='单价')),
                ('active', models.BooleanField(default=True, verbose_name='进行中')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.place')),
                ('serves', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.serves')),
            ],
            options={
                'verbose_name': '服务场所',
                'verbose_name_plural': '服务场所',
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='ServesMaids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField(default=90, verbose_name='单价')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('active', models.BooleanField(default=True, verbose_name='进行中')),
                ('maid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.maid')),
                ('serves', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.serves')),
            ],
            options={
                'verbose_name': '服务女仆',
                'verbose_name_plural': '服务女仆',
                'ordering': ['serves'],
            },
        ),
        migrations.CreateModel(
            name='ServesItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField(verbose_name='单价')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='数量')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.menu')),
                ('serves', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.serves')),
            ],
            options={
                'verbose_name': '服务项目',
                'verbose_name_plural': '服务项目',
                'ordering': ['serves'],
            },
        ),
        migrations.CreateModel(
            name='ServesCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='总额')),
                ('note', models.CharField(max_length=200, verbose_name='备注')),
                ('paid', models.BooleanField(default=False, verbose_name='已支付')),
                ('manual', models.IntegerField(default=0, verbose_name='核增、核减')),
                ('returned', models.BooleanField(default=False, verbose_name='返现')),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='reception.bill')),
                ('serves', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='reception.serves')),
            ],
            options={
                'verbose_name': '服务收款',
                'verbose_name_plural': '服务收款',
            },
        ),
        migrations.AddField(
            model_name='serves',
            name='item',
            field=models.ManyToManyField(through='reception.ServesItems', to='reception.Menu'),
        ),
        migrations.AddField(
            model_name='serves',
            name='maid',
            field=models.ManyToManyField(through='reception.ServesMaids', to='reception.Maid'),
        ),
        migrations.AddField(
            model_name='serves',
            name='place',
            field=models.ManyToManyField(through='reception.ServesPlaces', to='reception.Place'),
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('maid_NO', models.PositiveSmallIntegerField(default=1, verbose_name='女仆数')),
                ('active', models.BooleanField(default=True, verbose_name='有效')),
                ('advanced_payment', models.SmallIntegerField(verbose_name='定金')),
                ('through', models.CharField(choices=[('MP', '小程序'), ('WC', '微信'), ('PH', '电话'), ('MA', '女仆')], max_length=2, verbose_name='途径')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.customer')),
                ('maid', models.ManyToManyField(blank=True, to='reception.Maid')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reception.place')),
            ],
            options={
                'verbose_name': '预约',
                'verbose_name_plural': '预约',
            },
        ),
        migrations.CreateModel(
            name='MaidSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start', models.TimeField(verbose_name='上班')),
                ('end', models.TimeField(verbose_name='下班')),
                ('maid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.maid')),
            ],
            options={
                'verbose_name': '女仆排班',
                'verbose_name_plural': '女仆排班',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='DepositPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='会员卡扣款')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.deposit')),
            ],
            options={
                'verbose_name': '会员卡支付',
                'verbose_name_plural': '会员卡支付',
            },
        ),
        migrations.CreateModel(
            name='DepositCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='总额')),
                ('note', models.CharField(max_length=200, verbose_name='备注')),
                ('paid', models.BooleanField(default=False, verbose_name='已支付')),
                ('deposit_amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='储值金额')),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='reception.bill')),
            ],
            options={
                'verbose_name': '充值收款',
                'verbose_name_plural': '充值收款',
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reception.customer'),
        ),
        migrations.AddField(
            model_name='bill',
            name='deposit_payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reception.depositpayment'),
        ),
        migrations.AddField(
            model_name='bill',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reception.voucher'),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('WC', '微信扫码'), ('AP', '支付宝扫码'), ('MP', '小程序付款'), ('CS', '现金支付'), ('RE', '客服号转账')], max_length=2, verbose_name='支付方式')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='金额')),
                ('swift_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='流水号')),
                ('receiver', models.CharField(blank=True, max_length=100, null=True, verbose_name='核账人')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.bill')),
            ],
            options={
                'verbose_name': '入账',
                'verbose_name_plural': '入账',
                'unique_together': {('method', 'swift_number')},
            },
        ),
    ]
