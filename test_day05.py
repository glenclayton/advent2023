import pytest
import day05

def data():
    test_data =["seeds: 79 14 55 13",
"",
"seed-to-soil map:",
"50 98 2",
"52 50 48",
"",
"soil-to-fertilizer map:",
"0 15 37",
"37 52 2",
"39 0 15",
"",
"fertilizer-to-water map:",
"49 53 8",
"0 11 42",
"42 0 7",
"57 7 4",
"",
"water-to-light map:",
"88 18 7",
"18 25 70",
"",
"light-to-temperature map:",
"45 77 23",
"81 45 19",
"68 64 13",
"",
"temperature-to-humidity map:",
"0 69 1",
"1 0 69",
"",
"humidity-to-location map:",
"60 56 37",
"56 93 4"]
    return test_data

def test_sourcedestination():
    sd = day05.source_destination(50, 98, 2)
    idx = sd.mapSource(98)
    assert idx == 50
    idx = sd.mapSource(99)
    assert idx == 51
    idx = sd.mapSource(100)
    assert idx == -1
    idx = sd.mapSource(10)
    assert idx == -1

def test_agrimapparse():
    test_data = ['seed-to-soil map:\n','50 98 2\n','52 50 48\n']
    am = day05.agri_map(test_data)
    assert am.fromItem == 'seed'
    assert am.toItem == 'soil'
    assert len(am.maps) == 2
    idx = am.maps[0].mapSource(98)
    assert idx == 50
    idx = am.maps[1].mapSource(51)
    assert idx == 53
    idx = am.mapSource(98)
    assert idx == 50
    idx = am.mapSource(51)
    assert idx == 53
    idx = am.mapSource(1)
    assert idx == 1
    idx = am.mapSource(101)
    assert idx == 101

def test_parseseeds():
    test_data = ['seeds: 1 3 43 123\n','\n','seed-to-soil map:\n','50 98 2\n','52 50 48\n']
    alm = day05.almanac(test_data)
    assert len(alm.seeds) == 4
    assert alm.seeds[0] == 1
    assert alm.seeds[3] == 123

def test_parsealmanac():
    test_data = ['seeds: 1 3 43 123\n','\n','seed-to-soil map:\n','50 98 2\n','52 50 48\n']
    alm = day05.almanac(test_data)
    assert len(alm.agri_maps) == 1
    assert alm.agri_maps['seed'].fromItem == 'seed'
    assert alm.agri_maps['seed'].toItem == 'soil'

def test_parsealmanac_full():
    test_data = data()
    alm = day05.almanac(test_data)
    assert len(alm.seeds) == 4
    assert len(alm.agri_maps) == 7

def test_parsealmanac_full():
    test_data = data()
    alm = day05.almanac(test_data)
    location = alm.calculateNext('seed',79)
    assert location == 82
    location = alm.calculateNext('seed',14)
    assert location == 43
    location = alm.calculateNext('seed',55)
    assert location == 86
    location = alm.calculateNext('seed',13)
    assert location == 35
    minLocation = alm.minLocation()
    assert minLocation == 35
