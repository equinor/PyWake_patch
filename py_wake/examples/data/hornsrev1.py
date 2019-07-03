import numpy as np
from py_wake.site._site import UniformWeibullSite
from py_wake.wind_turbines import OneTypeWindTurbines

wt_x = [423974, 424042, 424111, 424179, 424247, 424315, 424384, 424452, 424534,
        424602, 424671, 424739, 424807, 424875, 424944, 425012, 425094, 425162,
        425231, 425299, 425367, 425435, 425504, 425572, 425654, 425722, 425791,
        425859, 425927, 425995, 426064, 426132, 426214, 426282, 426351, 426419,
        426487, 426555, 426624, 426692, 426774, 426842, 426911, 426979, 427047,
        427115, 427184, 427252, 427334, 427402, 427471, 427539, 427607, 427675,
        427744, 427812, 427894, 427962, 428031, 428099, 428167, 428235, 428304,
        428372, 428454, 428522, 428591, 428659, 428727, 428795, 428864, 428932,
        429014, 429082, 429151, 429219, 429287, 429355, 429424, 429492]
wt_y = [6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556,
        6151447, 6150891, 6150335, 6149779, 6149224, 6148668, 6148112, 6147556]
wt9_x = np.array(wt_x)[[0, 1, 2, 8, 9, 10, 16, 17, 18]]
wt9_y = np.array(wt_y)[[0, 1, 2, 8, 9, 10, 16, 17, 18]]


power_curve = np.array([[3.0, 0.0],
                        [4.0, 66.6],
                        [5.0, 154.0],
                        [6.0, 282.0],
                        [7.0, 460.0],
                        [8.0, 696.0],
                        [9.0, 996.0],
                        [10.0, 1341.0],
                        [11.0, 1661.0],
                        [12.0, 1866.0],
                        [13.0, 1958.0],
                        [14.0, 1988.0],
                        [15.0, 1997.0],
                        [16.0, 1999.0],
                        [17.0, 2000.0],
                        [18.0, 2000.0],
                        [19.0, 2000.0],
                        [20.0, 2000.0],
                        [21.0, 2000.0],
                        [22.0, 2000.0],
                        [23.0, 2000.0],
                        [24.0, 2000.0],
                        [25.0, 2000.0]])
ct_curve = np.array([[3.0, 0.0],
                     [4.0, 0.818],
                     [5.0, 0.806],
                     [6.0, 0.804],
                     [7.0, 0.805],
                     [8.0, 0.806],
                     [9.0, 0.807],
                     [10.0, 0.793],
                     [11.0, 0.739],
                     [12.0, 0.709],
                     [13.0, 0.409],
                     [14.0, 0.314],
                     [15.0, 0.249],
                     [16.0, 0.202],
                     [17.0, 0.167],
                     [18.0, 0.14],
                     [19.0, 0.119],
                     [20.0, 0.102],
                     [21.0, 0.088],
                     [22.0, 0.077],
                     [23.0, 0.067],
                     [24.0, 0.06],
                     [25.0, 0.053]])


class V80(OneTypeWindTurbines):
    def __init__(self):
        OneTypeWindTurbines.__init__(self, 'V80', diameter=80, hub_height=70,
                                     ct_func=self._ct, power_func=self._power, power_unit='kW')

    def _ct(self, u):
        return np.interp(u, ct_curve[:, 0], ct_curve[:, 1])

    def _power(self, u):
        return np.interp(u, power_curve[:, 0], power_curve[:, 1])


HornsrevV80 = V80


class Hornsrev1Site(UniformWeibullSite):
    def __init__(self):
        f = [3.597152, 3.948682, 5.167395, 7.000154, 8.364547, 6.43485,
             8.643194, 11.77051, 15.15757, 14.73792, 10.01205, 5.165975]
        a = [9.176929, 9.782334, 9.531809, 9.909545, 10.04269, 9.593921,
             9.584007, 10.51499, 11.39895, 11.68746, 11.63732, 10.08803]
        k = [2.392578, 2.447266, 2.412109, 2.591797, 2.755859, 2.595703,
             2.583984, 2.548828, 2.470703, 2.607422, 2.626953, 2.326172]
        UniformWeibullSite.__init__(self, f, a, k, .1)
        self.initial_position = np.array([wt_x, wt_y]).T


def main():
    wt = V80()
    print('Diameter', wt.diameter())
    print('Hub height', wt.hub_height())
    ws = np.arange(3, 25)
    import matplotlib.pyplot as plt
    plt.plot(ws, wt.power(ws), '.-')
    plt.show()


if __name__ == '__main__':
    main()
