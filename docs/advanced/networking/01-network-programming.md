<!-- Navigation -->
**[← Performance](../performance/01-performance-optimization.md)** | **[Back to Index](../../../README.md)** | **[AI Agents →](../ai-agents/01-langchain-langgraph.md)**

---

# Advanced Python: Network Programming

## 2.19 Socket Programming Basics

Sockets are endpoints for network communication. Python's `socket` module provides low-level networking.

### TCP Server and Client

```python
import socket

# TCP Server
def start_server(host='localhost', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")
            
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {data}")
            
            response = f"Echo: {data}"
            client_socket.send(response.encode('utf-8'))
            
            client_socket.close()
    finally:
        server_socket.close()

# TCP Client
def connect_client(host='localhost', port=5000, message='Hello'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    
    print(f"Server response: {response}")
    client_socket.close()

# Usage (in separate terminals)
# Terminal 1: start_server()
# Terminal 2: connect_client(message="Hello Server")
```

### UDP Communication

```python
import socket

# UDP Server
def udp_server(host='localhost', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    
    print(f"UDP Server listening on {host}:{port}")
    
    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Received from {address}: {data.decode('utf-8')}")
        
        response = b"Message received"
        server_socket.sendto(response, address)

# UDP Client
def udp_client(host='localhost', port=5000, message='Hello'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    client_socket.sendto(message.encode('utf-8'), (host, port))
    response, _ = client_socket.recvfrom(1024)
    
    print(f"Response: {response.decode('utf-8')}")
    client_socket.close()
```

---

## 2.20 HTTP Requests

### Using requests Library

```python
import requests

# GET request
response = requests.get('https://api.example.com/users')
print(f"Status: {response.status_code}")
print(f"Data: {response.json()}")

# POST request
data = {"name": "Alice", "email": "alice@example.com"}
response = requests.post('https://api.example.com/users', json=data)
print(response.json())

# Headers and authentication
headers = {"User-Agent": "MyApp/1.0"}
auth = ("username", "password")
response = requests.get('https://api.example.com/protected', headers=headers, auth=auth)

# Query parameters
params = {"page": 1, "limit": 20}
response = requests.get('https://api.example.com/items', params=params)

# File upload
files = {'file': open('document.pdf', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)

# Timeout and error handling
try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raise exception for 4xx/5xx
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### Session Management

```python
import requests

# Create session for connection pooling
session = requests.Session()
session.headers.update({"Authorization": "Bearer token123"})

# Multiple requests reuse connection
for i in range(5):
    response = session.get(f'https://api.example.com/user/{i}')
    print(response.json())

session.close()
```

---

## 2.21 Async HTTP with aiohttp

```python
import asyncio
import aiohttp

async def fetch_user(session, user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        return None

async def fetch_multiple_users(user_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session, user_id) for user_id in user_ids]
        results = await asyncio.gather(*tasks)
        return results

# Usage
user_ids = [1, 2, 3, 4, 5]
results = asyncio.run(fetch_multiple_users(user_ids))

for user in results:
    if user:
        print(f"User: {user['name']}, Email: {user['email']}")
```

### Timeout and Retry Logic

```python
import asyncio
import aiohttp
from aiohttp import ClientError

async def fetch_with_retry(url, max_retries=3, timeout=5):
    timeout_obj = aiohttp.ClientTimeout(total=timeout)
    
    for attempt in range(max_retries):
        try:
            async with aiohttp.ClientSession(timeout=timeout_obj) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status >= 500:
                        print(f"Server error, retrying... (attempt {attempt+1})")
                    else:
                        return None
        except (ClientError, asyncio.TimeoutError) as e:
            print(f"Error: {e}, retrying... (attempt {attempt+1})")
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise

# Usage
# result = asyncio.run(fetch_with_retry('https://api.example.com/data'))
```

---

## 2.22 DNS and Hostname Resolution

```python
import socket

# Resolve hostname to IP
hostname = 'example.com'
ip_address = socket.gethostbyname(hostname)
print(f"{hostname} -> {ip_address}")

# Reverse DNS lookup
try:
    hostname_result, aliases, addresses = socket.gethostbyaddr(ip_address)
    print(f"Reverse: {ip_address} -> {hostname_result}")
except socket.herror as e:
    print(f"Reverse lookup failed: {e}")

# Get all addresses for a hostname
addresses_info = socket.getaddrinfo('example.com', 443)
for family, socktype, proto, canonname, sockaddr in addresses_info:
    print(f"Address: {sockaddr[0]}")
```

---

## 2.23 Real-World Example: Web Scraper with Error Handling

```python
import aiohttp
import asyncio
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebScraper:
    def __init__(self, max_concurrent=5, timeout=10):
        self.max_concurrent = max_concurrent
        self.timeout = timeout
        self.session = None
    
    async def __aenter__(self):
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        self.session = aiohttp.ClientSession(timeout=timeout)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
    
    async def fetch_page(self, url: str) -> Dict:
        """Fetch single page with error handling"""
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        async with semaphore:
            try:
                async with self.session.get(url) as response:
                    if response.status == 200:
                        return {
                            'url': url,
                            'status': response.status,
                            'content': await response.text(),
                            'error': None
                        }
                    else:
                        logger.warning(f"Status {response.status} for {url}")
                        return {
                            'url': url,
                            'status': response.status,
                            'content': None,
                            'error': f"HTTP {response.status}"
                        }
            except asyncio.TimeoutError:
                logger.error(f"Timeout fetching {url}")
                return {
                    'url': url,
                    'status': None,
                    'content': None,
                    'error': "Timeout"
                }
            except Exception as e:
                logger.error(f"Error fetching {url}: {e}")
                return {
                    'url': url,
                    'status': None,
                    'content': None,
                    'error': str(e)
                }
    
    async def fetch_multiple(self, urls: List[str]) -> List[Dict]:
        """Fetch multiple URLs concurrently"""
        tasks = [self.fetch_page(url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage
async def main():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://github.com"
    ]
    
    async with WebScraper(max_concurrent=3) as scraper:
        results = await scraper.fetch_multiple(urls)
        
        for result in results:
            if result['error']:
                print(f"❌ {result['url']}: {result['error']}")
            else:
                print(f"✓ {result['url']}: {len(result['content'])} bytes")

# asyncio.run(main())
```

---

## 2.24 Port Scanning and Network Utilities

```python
import socket
import threading
from typing import List

def scan_port(host: str, port: int, timeout: float = 1) -> bool:
    """Check if port is open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        return False
    except socket.error:
        return False

def scan_ports(host: str, ports: List[int], threads: int = 5) -> List[int]:
    """Scan multiple ports concurrently"""
    open_ports = []
    
    def worker(port_queue):
        while not port_queue.empty():
            port = port_queue.get()
            if scan_port(host, port):
                open_ports.append(port)
                print(f"Port {port}: OPEN")
            port_queue.task_done()
    
    import queue
    port_queue = queue.Queue()
    
    for port in ports:
        port_queue.put(port)
    
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker, args=(port_queue,))
        t.start()
        thread_list.append(t)
    
    for t in thread_list:
        t.join()
    
    return sorted(open_ports)

# Usage
# common_ports = [21, 22, 25, 53, 80, 443, 3306, 5432, 8080]
# open_ports = scan_ports('example.com', common_ports)
# print(f"Open ports: {open_ports}")
```

---

## 2.25 Email Sending

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender: str, password: str, recipient: str, 
               subject: str, body: str, attachments: list = None):
    """Send email with optional attachments"""
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Add attachments
    if attachments:
        for file_path in attachments:
            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {file_path}')
                msg.attach(part)
    
    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# Usage
# send_email(
#     sender='your_email@gmail.com',
#     password='your_app_password',
#     recipient='recipient@example.com',
#     subject='Hello',
#     body='This is a test email',
#     attachments=['document.pdf']
# )
```

---

## 2.26 SSL/TLS Certificates

```python
import ssl
import socket
from datetime import datetime

def check_certificate(hostname: str, port: int = 443):
    """Check SSL certificate details"""
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                print(f"Certificate for {hostname}:")
                print(f"Subject: {dict(x[0] for x in cert['subject'])}")
                print(f"Issuer: {dict(x[0] for x in cert['issuer'])}")
                
                # Parse expiration date
                not_after = cert['notAfter']
                print(f"Valid until: {not_after}")
                
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Usage
# check_certificate('example.com')
```

---

## Mini-Exercise: Simple Chat Application

```python
import socket
import threading

class SimpleChatServer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []
    
    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        
        print(f"Chat server started on {self.host}:{self.port}")
        
        try:
            while True:
                client_socket, address = self.server_socket.accept()
                self.clients.append(client_socket)
                print(f"Client connected: {address}")
                
                thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                thread.daemon = True
                thread.start()
        finally:
            self.server_socket.close()
    
    def handle_client(self, client_socket, address):
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                message = f"{address}: {data}"
                print(message)
                
                # Broadcast to all clients
                self.broadcast(message, client_socket)
        except:
            pass
        finally:
            self.clients.remove(client_socket)
            client_socket.close()
            print(f"Client disconnected: {address}")
    
    def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    pass

class SimpleChatClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        
        # Receive messages in background
        thread = threading.Thread(target=self.receive_messages)
        thread.daemon = True
        thread.start()
        
        # Send messages
        while True:
            message = input("You: ")
            if message.lower() == 'exit':
                break
            self.socket.send(message.encode('utf-8'))
        
        self.socket.close()
    
    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n{message}\nYou: ", end='')
            except:
                break

# Usage
# Server: SimpleChatServer().start()
# Clients: SimpleChatClient().connect()
```

---

## Summary Table

| Concept | Purpose | Module |
|---------|---------|--------|
| **TCP/UDP Sockets** | Low-level networking | `socket` |
| **HTTP Requests** | REST API calls | `requests` |
| **Async HTTP** | Concurrent requests | `aiohttp` |
| **DNS** | Hostname resolution | `socket` |
| **Port Scanning** | Network discovery | `socket` + `threading` |
| **Email** | Send messages | `smtplib`, `email` |
| **SSL/TLS** | Secure connections | `ssl` |

| Task | Library | Speed |
|------|---------|-------|
| Single HTTP request | `requests` | Good |
| Multiple HTTP requests | `aiohttp` | Excellent |
| TCP server | `socket` | Low-level |
| HTTP server | `FastAPI`, `Flask` | High-level |
| Async HTTP server | `FastAPI` | Excellent |

---

<!-- Navigation Footer -->
**[← Performance](../performance/01-performance-optimization.md)** | **[Back to Index](../../../README.md)** | **[AI Agents →](../ai-agents/01-langchain-langgraph.md)**

**Sections:** 2.19-2.26 | **Time:** 1-2 hours
