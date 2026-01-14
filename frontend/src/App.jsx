import { useState } from 'react'
import './index.css'
import { RotatingLines } from 'react-loader-spinner'

function Loader() {
    return (
        <RotatingLines
            strokeColor="#0a80daf6"
            strokeWidth="5"
            animationDuration="1200"
            width="30"
            visible={true}
        />
    )
}

function App() {
    const [ticketText, setTicketText] = useState('')
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)
    const [result, setResult] = useState(null)

    const handleSubmit = async (e) => {
        e.preventDefault()
        setLoading(true)
        setError(null)
        setResult(null)

        try {
            const response = await fetch('http://localhost:8000/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ ticket_text: ticketText })
            })

            if (!response.ok) {
                throw new Error('Failed to analyze ticket')
            }
            const data = await response.json()
            setResult(data)
        } catch (error) {
            setError(error.message)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className='container'>
            <h1>AI Conversation Summarizer</h1>
            <div className='form-section'>
                <form onSubmit={handleSubmit}>
                    <textarea
                        value={ticketText}
                        onChange={(e) => setTicketText(e.target.value)}
                        placeholder='Enter ticket text here'
                        required
                    ></textarea>
                    <button type='submit' disabled={loading || !ticketText.trim()}>
                        {loading ? 'Analyzing...' : 'Analyze'}
                    </button>
                </form>
            </div>

            {error && (
                <div className="error">Error: {error}</div>
            )}

            {loading && (
                <div className='loading'>
                    <Loader />
                    <p> Analyzing with AI...</p>
                </div>
            )}

            {result && (
                <div className='result-section'>
                    <div className='result-item'>
                        <h3>✨ AI Overview</h3>
                        <p style={{ whiteSpace: 'pre-wrap' }}>{result.summary}</p>
                    </div>
                </div>
            )}
        </div>
    )
}
export default App