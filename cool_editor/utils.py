from redis import StrictRedis


class DecodedRedis(StrictRedis):
    @classmethod
    def from_url(cls, url, db=None, **kwargs):
        kwargs['decode_responses'] = True
        return StrictRedis.from_url(url, db, **kwargs)
