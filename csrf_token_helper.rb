# DISTRACTOR: csrf_token_helper.rb contains 'token' as substring
# but basename fails the anchored ^token(s)?(\.[a-z]+)?$ rule.
def csrf_token_for(uid):
    return "synthetic_csrf_" + uid