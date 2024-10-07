from datetime import datetime


class SharpApiSubscriptionInfo:
    def __init__(self, data):
        self.timestamp = datetime.fromisoformat(data['timestamp'])
        self.on_trial = data['on_trial']
        self.trial_ends = datetime.fromisoformat(data['trial_ends'])
        self.subscribed = data['subscribed']
        self.current_subscription_start = datetime.fromisoformat(data['current_subscription_start'])
        self.current_subscription_end = datetime.fromisoformat(data['current_subscription_end'])
        self.subscription_words_quota = data['subscription_words_quota']
        self.subscription_words_used = data['subscription_words_used']
        self.subscription_words_used_percentage = data['subscription_words_used_percentage']

