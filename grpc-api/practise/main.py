import sys
import proto.account_pb2 as account_pb
import proto.user_pb2 as user_pb

def account():
    return account_pb.Account(
        id=43,
        name='linus torvalds',
        is_verified=True,
        follow_ids=[2,3,4,5],
    )

def user():
    return user_pb.User(
        id=43,
        name='Linus torvalds',
        follows=[
            user_pb.User(id=1, name='Linux Foundation'),
            user_pb.User(id=2, name='Clement Jean')
        ],
    )

def user2():
    u = user_pb.User()
    u.id = 43
    u.name = 'Linus torvalds'
    u.follows.add(id=1, name='Linux Foundation')
    u.follows.add(id=2, name='Clement Jean')
    return u


if __name__ == '__main__':
    fns = {
        'account': account,
        'user': user,
        'user2': user2,
    }

    if len(sys.argv) != 2:
        print(f'Usage: main.py [{"|".join(fns)}]')
        sys.exit()

    fn = fns.get(sys.argv[1], None)

    if not fn:
        print(f'Unknown function \"{sys.argv[1]}\"')
        sys.exit()
    
    print(fn())