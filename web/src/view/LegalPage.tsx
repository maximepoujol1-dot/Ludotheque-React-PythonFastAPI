import React from 'react'
import Card from '../components/Card'

const cardStyle = "w-full max-w-3xl mx-auto p-8 bg-white dark:bg-dark-surface text-gray-700 dark:text-gray-300 shadow-xl border border-gray-200 dark:border-white/10 border-t-4 border-t-green-500 rounded-2xl"

const LegalPage = () => {
  return (
    <div className="flex flex-col gap-8 px-4 py-12 bg-white dark:bg-dark-bg min-h-screen">
        <section id="condition">
          <br/>            
            <Card title={"Condition"} style={cardStyle}>
              <p>explication</p>
            </Card>
          <br/>            
        </section>

        <section id="confidentialité">
          <br/>
            <Card title={"Confidentialité"} style={cardStyle}>
              <p>explication</p>
            </Card>
          <br/>
        </section>

        <section id="menteion">
          <br/>
            <Card title={"Mentions légales"} style={cardStyle}>
              <p>explication</p>
            </Card>          
          <br/>
        </section>
    </div>
  )
}

export default LegalPage