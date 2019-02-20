import statistics
a_list = [1,2,3.2,1.8,19,10]
print(statistics.pstdev(a_list))#これは母集団が測定可能な時に使う。母集団の標準偏差。

print(statistics.stdev(a_list))#これは母集団が測定不可能な時に使う。母集団の不偏推定量。
#データ數が充分にないと推定の正確性が下がる。俗にいう標本標準偏差。

print(statistics.pvariance(a_list))#測定可能。1番目と同じ。母集団の分散。

print(statistics.variance(a_list))#測定不可能。2番目と同じ。俗にいう不偏分散。

#標本そのものの標準偏差、分散は求める必要性なし。

#標本の数が多くなれば多くなるほど、標本標準偏差の平均　＝　母集団の標準偏差(分散も同じ	))

import cobed
cobed.challenge(10)
