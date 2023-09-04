import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Web tutorials',
  description: 'Generated by Minyoung',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
          <li><a href="/read/1">HTML</a></li>
          <li><a href="/read/2">CSS</a></li>
        </ol>
        {children}
        <ul>
          <li><a href="/create">Create</a></li>
          <li><a href="/update/1">Update</a></li>
          <li><input type="button" value="delete" /></li>
        </ul>
      </body>
    </html>
  )
}