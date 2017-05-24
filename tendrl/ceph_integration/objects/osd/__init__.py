from tendrl.commons import objects


class Osd(objects.BaseObject):
    def __init__(self, id=None,
                 uuid=None, public_addr=None, cluster_addr=None,
                 heartbeat_front_addr=None, heartbeat_back_addr=None,
                 down_at=None, up_from=None, lost_at=None,
                 osd_up=None, osd_in=None, up_thru=None,
                 weight=None, primary_affinity=None,
                 state=None, last_clean_begin=None,
                 last_clean_end=None, *args, **kwargs):
        super(Osd, self).__init__(*args, **kwargs)

        self.id = id
        self.uuid = uuid
        self.public_addr = public_addr
        self.cluster_addr = cluster_addr
        self.heartbeat_front_addr = heartbeat_front_addr
        self.heartbeat_back_addr = heartbeat_back_addr
        self.down_at = down_at
        self.up_from = up_from
        self.lost_at = lost_at
        self.osd_up = osd_up
        self.osd_in = osd_in
        self.up_thru = up_thru
        self.weight = weight
        self.primary_affinity = primary_affinity
        self.state = state
        self.last_clean_begin = last_clean_begin
        self.last_clean_end = last_clean_end
        self.value = 'clusters/{0}/Osds/{1}'

    def render(self):
        self.value = self.value.format(
            NS.tendrl_context.integration_id,
            self.uuid
        )
        return super(Osd, self).render()
