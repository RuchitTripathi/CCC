mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

echo "\
[logger]\n\
level = 'error'\n\
" >> ~/.streamlit/config.toml

echo "\
[server]\n\
requireLogin = true\n\
" >> ~/.streamlit/config.toml