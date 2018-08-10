weekT={'h':'thursday',
       'u':'tuesday'}
weekS={'a':'saturday',
       'u':'sunday'}
week={'t':weekT,
      's':weekS,
      'm':'monday',
      'w':'wensday',
      'f':'friday'}
a=week[str(input('请输入第一位字母:')).lower()]
if a==weekT or a==weekS:
    print(a[str(input('请输入第二位字母:')).lower()])
else:
    print(a)
