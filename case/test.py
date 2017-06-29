from cap.parse_cap import PcapService


def create_test_case(cap_file='unified_cache_server.cap', step=100, r=0):
    ps = PcapService(cap_file)
    post_data = ps.get_udp_data(step, r)
    return post_data

if __name__ == '__main__':
    tests = create_test_case('unified_cache_server.cap', 100, 2)
    for t in tests:
        print t.id, t.seq
        print t.request

