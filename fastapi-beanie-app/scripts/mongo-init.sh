#!/usr/bin/sh
set -e

mongo <<EOF

db.createUSer({
    user: '${MONGODB_APP_USERNAME}',
    pwd: '${MONGODB_APP_PASSWORD}'
});
EOF