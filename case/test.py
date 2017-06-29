from cap.parse_cap import PcapService


def create_test_case(cap_file='unified_cache_server.cap', step=100, r=0, f=None):
    ps = PcapService(cap_file)
    post_data = ps.get_udp_data(step, r, f)
    return post_data




