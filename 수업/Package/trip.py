# import Travel.France
# # import Travel.England
# from Travel import * # Travel 패키지 안에 모든걸 가져올게
#
# # trip_to 객체 생성
# trip_to = France.FrancePackage()
# trip_to.detail()
#
# # trip_to2 객체 생성
# trip_to2 = England.EnglandPackage()
# trip_to2.detail()

from Travel.France import FrancePackage

trip_to = FrancePackage()
trip_to.detail()