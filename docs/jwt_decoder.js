//  decodificación de payload de JWT
const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
const payload = token.split('.')[1]
const base64 = payload.replace(/-/g,'+').replace(/_/g,'/');
decodeURIComponent(window.atob(base64).split('').map((caracter)=> '%' +('00'+ caracter.charCodeAt(0).toString(16)).slice(-2)).join(''))