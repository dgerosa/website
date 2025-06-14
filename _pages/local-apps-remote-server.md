---
layout: archive
title: "Local apps from a remote server"
permalink: /local-apps-remote-server/
redirect_from:
  - /local-browser-on-ssh-tunnel/
  - /local-browser-remote-server/
---

This is a short guide to access remote resources with your local (i.e. laptopt) machine. Includes browsing the internet and using jupyter notebooks

## Browse the internet

Let's browse the internet using a local browser via a remote server. This is useful to login into a University machine with your RSA key and then use your laptopt as if you are on campus.

### Option 1 (best): a dedicated Chrome session

The best option I found was to open a dedicated Chrome session through an SSH tunnel. First, open an ssh connection to your server (`user@host`) specifying the port number (in this case 1337 but you can pick whatever you want):

```
ssh -D 1337 -f -C -q -N user@host
```

Then open Google Chrome using that SSH tunnel as a proxy. You need to specify a cache directory; otherwise, it interferes with your main Chrome session:

```
ssh -D $portid -f -C -q -N $host /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --proxy-server=socks5://localhost:1337 --user-data-dir=~/chromesession`
```

A new Chrome window will open: in that window (but not elsewhere) it’s like you’re browsing from the remote location. Wow!

You can put these two operations in a convenient function for your `bashrc`

```
function portssh {
       host=${1}
       portid=${2:-1337}
       echo Port $portid $host
       ssh -D $portid -f -C -q -N $host
       /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --proxy-server=socks5://localhost:${portid} --user-data-dir=/Users/dgerosa/Library/otherchromesession
```

This can be called with

```
portssh <server>
```

where `<server>` is an entry of your ssh config file.

### Option 2 (manual): a global proxy

This is a more manual solution where you redirect the entire web traffic through the remote server. First open the ssh tunnel

```
ssh -D 1337 -f -C -q -N user@host
```

On mac then do the following:

*   Go to: “Settings”, “Network”, “Wi-Fi”, “Advanced”, “Proxies”.
*   Click on “SOCKS Proxies” and write “localhost” and “1337” in the two white boxes separated by a colon.
*   Click “Ok” and “Apply”

Here you go, your browser will now believe you’re elsewhere. Remember you switch the proxy option off when you want to go back to your usual internet setup.

## Jupyter notebooks

This is to run [remote instances of jupyter notebooks](https://stackoverflow.com/questions/69244218/how-to-run-a-jupyter-notebook-through-a-remote-server-on-local-machine), such that the visual interface is provided by your own laptop but the calculations in the background are done on the servers.
 
- From your local machine (say your laptop), login into the remote server while providing a specific port number. For instance (assuming `<server>` is an entry of your ssh config file):

```
ssh -L 8080:localhost:8080 xwing
```

The number 8080 is just an example, pick a different port as only one user can use a given port at once.

- On the remote server, run jupyter while sending outputs to that port:

```
jupyter notebook --no-browser --port=8080
```

- Jupyter will print a web url to screen. Just paste that into your local browser and you should be good to go.

