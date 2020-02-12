from numpy.testing import assert_almost_equal
from pypfopt.risk_models import sample_cov
import pytest
from mcos.denoising import denoise_conv


@pytest.mark.parametrize('q, bandwidth', [(.5, .25), (1.5, .9), (4.5, 1.9)])
def test_de_noise_cov(q, bandwidth, covariance_matrix, expected_results):
    results = denoise_conv.de_noise_cov(covariance_matrix, q, bandwidth)
    assert results.shape == (20, 20)
    assert_almost_equal(results.min(), 0.013728494161889633)
    assert_almost_equal(results.max(), 0.39058571400929504)
    assert_almost_equal(results, expected_results)


@pytest.fixture
def covariance_matrix(prices_df):
    return sample_cov(prices_df).values


@pytest.fixture
def expected_results():
    return [[0.09321114, 0.03629861, 0.02013626, 0.02095464, 0.04909072, 0.03121522,
             0.0501403, 0.02199346, 0.0465604, 0.0250841, 0.02217497, 0.04773557,
             0.04426075, 0.02251443, 0.03667345, 0.03966196, 0.0373206, 0.02428323,
             0.04238822, 0.03489314],
            [0.03629861, 0.20753691, 0.02378114, 0.02474766, 0.05797667, 0.03686551,
             0.05921623, 0.02597451, 0.05498833, 0.0296246, 0.02618888, 0.05637622,
             0.05227242, 0.02658979, 0.04331174, 0.0468412, 0.04407603, 0.02867875,
             0.05006094, 0.04120917],
            [0.02013626, 0.02378114, 0.13720115, 0.01372849, 0.03216192, 0.02045074,
             0.03284956, 0.01440908, 0.03050418, 0.01643392, 0.01452799, 0.03127409,
             0.02899756, 0.01475039, 0.02402672, 0.02598465, 0.0244507, 0.01590923,
             0.02777076, 0.02286034],
            [0.02095464, 0.02474766, 0.01372849, 0.10095819, 0.03346906, 0.0212819,
             0.03418464, 0.01499469, 0.03174394, 0.01710183, 0.01511845, 0.03254514,
             0.03017608, 0.01534988, 0.02500322, 0.02704072, 0.02544443, 0.01655581,
             0.02889943, 0.02378943],
            [0.04909072, 0.05797667, 0.03216192, 0.03346906, 0.37539405, 0.04985739,
             0.08008481, 0.03512826, 0.07436694, 0.04006469, 0.03541818, 0.07624394,
             0.0706939, 0.03596037, 0.05857537, 0.06334865, 0.05960899, 0.03878552,
             0.06770307, 0.05573182],
            [0.03121522, 0.03686551, 0.02045074, 0.0212819, 0.04985739, 0.08310901,
             0.05092336, 0.02233694, 0.04728755, 0.02547585, 0.02252129, 0.04848108,
             0.04495199, 0.02286605, 0.0372462, 0.04028138, 0.03790345, 0.02466247,
             0.04305021, 0.03543808],
            [0.0501403, 0.05921623, 0.03284956, 0.03418464, 0.08008481, 0.05092336,
             0.39058571, 0.03587932, 0.07595693, 0.04092129, 0.03617544, 0.07787406,
             0.07220537, 0.03672922, 0.05982773, 0.06470308, 0.06088346, 0.03961477,
             0.06915059, 0.05692339],
            [0.02199346, 0.02597451, 0.01440908, 0.01499469, 0.03512826, 0.02233694,
             0.03587932, 0.06909179, 0.03331762, 0.01794965, 0.01586793, 0.03415855,
             0.03167204, 0.01611084, 0.02624274, 0.02838125, 0.02670582, 0.01737656,
             0.0303321, 0.02496878],
            [0.0465604, 0.05498833, 0.03050418, 0.03174394, 0.07436694, 0.04728755,
             0.07595693, 0.03331762, 0.18019232, 0.0379996, 0.03359259, 0.07231404,
             0.06705007, 0.03410684, 0.05555617, 0.06008343, 0.05653652, 0.03678637,
             0.0642134, 0.05285919],
            [0.0250841, 0.0296246, 0.01643392, 0.01710183, 0.04006469, 0.02547585,
             0.04092129, 0.01794965, 0.0379996, 0.08011557, 0.01809779, 0.0389587,
             0.03612278, 0.01837483, 0.02993052, 0.03236954, 0.03045867, 0.01981841,
             0.03459454, 0.02847753],
            [0.02217497, 0.02618888, 0.01452799, 0.01511845, 0.03541818, 0.02252129,
             0.03617544, 0.01586793, 0.03359259, 0.01809779, 0.06555993, 0.03444046,
             0.03193343, 0.01624381, 0.02645932, 0.02861548, 0.02692622, 0.01751997,
             0.03058243, 0.02517485],
            [0.04773557, 0.05637622, 0.03127409, 0.03254514, 0.07624394, 0.04848108,
             0.07787406, 0.03415855, 0.07231404, 0.0389587, 0.03444046, 0.24552417,
             0.0687424, 0.03496769, 0.05695839, 0.06159991, 0.05796349, 0.03771485,
             0.06583413, 0.05419334],
            [0.04426075, 0.05227242, 0.02899756, 0.03017608, 0.0706939, 0.04495199,
             0.07220537, 0.03167204, 0.06705007, 0.03612278, 0.03193343, 0.0687424,
             0.32116207, 0.03242228, 0.05281222, 0.05711587, 0.05374415, 0.03496947,
             0.06104186, 0.05024844],
            [0.02251443, 0.02658979, 0.01475039, 0.01534988, 0.03596037, 0.02286605,
             0.03672922, 0.01611084, 0.03410684, 0.01837483, 0.01624381, 0.03496769,
             0.03242228, 0.05440377, 0.02686437, 0.02905354, 0.02733842, 0.01778817,
             0.0310506, 0.02556023],
            [0.03667345, 0.04331174, 0.02402672, 0.02500322, 0.05857537, 0.0372462,
             0.05982773, 0.02624274, 0.05555617, 0.02993052, 0.02645932, 0.05695839,
             0.05281222, 0.02686437, 0.27222973, 0.04732491, 0.04453118, 0.02897491,
             0.0505779, 0.04163472],
            [0.03966196, 0.0468412, 0.02598465, 0.02704072, 0.06334865, 0.04028138,
             0.06470308, 0.02838125, 0.06008343, 0.03236954, 0.02861548, 0.06159991,
             0.05711587, 0.02905354, 0.04732491, 0.26954874, 0.04816001, 0.03133606,
             0.05469948, 0.04502752],
            [0.0373206, 0.04407603, 0.0244507, 0.02544443, 0.05960899, 0.03790345,
             0.06088346, 0.02670582, 0.05653652, 0.03045867, 0.02692622, 0.05796349,
             0.05374415, 0.02733842, 0.04453118, 0.04816001, 0.12030304, 0.0294862,
             0.0514704, 0.04236941],
            [0.02428323, 0.02867875, 0.01590923, 0.01655581, 0.03878552, 0.02466247,
             0.03961477, 0.01737656, 0.03678637, 0.01981841, 0.01751997, 0.03771485,
             0.03496947, 0.01778817, 0.02897491, 0.03133606, 0.0294862, 0.08550166,
             0.03349002, 0.02756832],
            [0.04238822, 0.05006094, 0.02777076, 0.02889943, 0.06770307, 0.04305021,
             0.06915059, 0.0303321, 0.0642134, 0.03459454, 0.03058243, 0.06583413,
             0.06104186, 0.0310506, 0.0505779, 0.05469948, 0.0514704, 0.03349002,
             0.14689262, 0.04812259],
            [0.03489314, 0.04120917, 0.02286034, 0.02378943, 0.05573182, 0.03543808,
             0.05692339, 0.02496878, 0.05285919, 0.02847753, 0.02517485, 0.05419334,
             0.05024844, 0.02556023, 0.04163472, 0.04502752, 0.04236941, 0.02756832,
             0.04812259, 0.15258853]]
