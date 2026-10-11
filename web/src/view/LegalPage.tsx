import React from 'react'
import Card from '../components/Card'

const cardStyle = "w-full max-w-3xl mx-auto p-8 bg-white dark:bg-dark-surface text-gray-700 dark:text-gray-300 shadow-xl border border-gray-200 dark:border-white/10 border-t-4 border-t-green-500 rounded-2xl"

const LegalPage = () => {
  return (
    <div className="flex flex-col gap-8 px-4 py-12 bg-white dark:bg-dark min-h-screen">
      <section id="condition">
        <br />
        <Card title={"Terms of Use"} style={cardStyle}>
          <div className="space-y-4 text-sm leading-7">
            <p>
              By accessing Ludothèque, you agree to comply with these Terms of Use. The application is
              designed to manage and present a board game collection, make it easier to consult game details,
              and keep track of favorites, loans, and personal interests.
            </p>
            <p>
              You agree to use the service responsibly and not to interfere with the platform's operation,
              compromise its security, or use it for fraudulent, unlawful, or abusive purposes. User-submitted
              content must respect the rights of others and basic standards of courtesy and legality.
            </p>
            <p>
              We reserve the right to modify, suspend, or discontinue all or part of the service at any time,
              including for technical, maintenance, or project evolution reasons. The information provided on the
              site is for informational purposes only and may be updated without prior notice.
            </p>
          </div>
        </Card>
        <br />
      </section>

      <section id="confidentialité">
        <br />
        <Card title={"Privacy Policy"} style={cardStyle}>
          <div className="space-y-4 text-sm leading-7">
            <p>
              User privacy is a priority. We collect only the data necessary for the proper functioning of the
              application, including account information, browsing preferences, and technical data required for
              security and service improvement.
            </p>
            <p>
              No passwords are stored in clear text in the database. Passwords are handled securely using
              appropriate hashing and protection mechanisms, in accordance with current security practices.
            </p>
            <p>
              Personal data is never sold or shared with third parties, except when required by law or when it is
              strictly necessary to provide the service. You may request access to, correction of, or deletion of
              your personal information by contacting us using the details provided in the legal notice.
            </p>
            <p>
              We implement reasonable safeguards to protect data against unauthorized access, modification, or
              disclosure. However, no internet transmission is entirely risk-free, and we cannot guarantee absolute
              security.
            </p>
          </div>
        </Card>
        <br />
      </section>

      <section id="mentions">
        <br />
        <Card title={"Legal Notice"} style={cardStyle}>
          <div className="space-y-4 text-sm leading-7">
            <p>
              <strong>Website publisher:</strong> Ludothèque, a project developed to manage and showcase a board
              game collection.
            </p>
            <p>
              <strong>Publication manager:</strong> the project development team, responsible for updating and
              maintaining the content of the site.
            </p>
            <p>
              <strong>Contact:</strong> you can contact us using the contact form available on the site or through
              the communication channels provided within the application.
            </p>
            <p>
              <strong>Hosting:</strong> the website is hosted by a third-party provider for now.
            </p>
            <p>
              The content and visual elements presented on this site remain the property of the project or the
              relevant authors. Any reproduction, even partial, requires prior authorization.
            </p>
            <p>
              For more information regarding the ownership and licensing of the project, please refer to the license
              made available on the project GitHub repository.
            </p>
          </div>
        </Card>
        <br />
      </section>
    </div>
  )
}

export default LegalPage