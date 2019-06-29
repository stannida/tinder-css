import pynder
X_Auth_Token = '1fe12968-4672-412f-883b-cdf0c516c449'
session = pynder.Session(XAuthToken=X_Auth_Token)
print(session.profile)
