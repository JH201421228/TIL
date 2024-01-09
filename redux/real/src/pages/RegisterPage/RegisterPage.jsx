import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import { createUserWithEmailAndPassword, getAuth, updateProfile } from 'firebase/auth'
import { set, ref } from 'firebase/database'
import app, { db } from '../../firebase'
import md5 from 'md5'

const RegisterPage = () => {
    const [loading, setLoading] = useState(false)

    const [errorFromSubmit, setErrorFromSubmit] =useState("")

    const auth = getAuth(app)

    const {register, watch, formState:{errors}, handleSubmit} = useForm()


    const onSubmit = async(data) => {
        try {
            setLoading(true)
            const createUser = await createUserWithEmailAndPassword(auth, data.email, data.password)
            const updatedUser = await updateProfile(auth.currentUser, {
                displayName: data.name,
                photoURL: `http://gravatar.com/avatar/${md5(createUser.user.email)}?d=identicon`
            })
            console.log(createUser)
            console.log(auth.currentUser)

            set(ref(db, `users/${createUser.user.uid}`), {
                name: createUser.user.displayName,
                image: createUser.user.photoURL
            })

        }
        catch (error) {
            console.error(error)
            setErrorFromSubmit(error.message)
            setTimeout(() => {
                setErrorFromSubmit("")
            }, 3000)
        }
        finally {
            setLoading(false)
        }
    }
    
  return (
    <div className='auth-wrapper'>
        <div style={{ textAlign: 'center' }}>
            <h3>Register</h3>
        </div>
        <form onSubmit={handleSubmit(onSubmit)}>
            <label htmlFor='email'>Email</label>
            <input 
                name='email'
                type='email'
                id='email'
                {...register("email", {required: true, pattern: /^\S+@\S+$/i})}
            />
            {errors.email && <p>This email field is required</p>}

            <label htmlFor="name">Name</label>
            <input 
                type="text" 
                name='name'
                id='name'
                {...register("name", {required: true, maxLength: 10})}
            />
            {errors.name && errors.name.type === "required" && <p>This name field is required</p>}
            {errors.name && errors.name.type === "maxLength" && <p>Your input exceed maximun length</p>}

            <label htmlFor="password">Password</label>
            <input 
                name='password'
                type="password" 
                id='password'
                {...register("password", {required: true, minLength: 6})}
            />
            {errors.password && errors.password.type === "required" && <p>This password field is required</p>}
            {errors.password && errors.password.type === "maxLength" && <p>Password must have at least 6 characters</p>}

            {errorFromSubmit && <p>{errorFromSubmit}</p>}

            <input type="submit" disabled = {loading} />
            <Link style={{color: 'grey', textDecoration: 'none'}} to={'/login'}>이미 아이디가 있다면...</Link>
        </form>
    </div>
  )
}

export default RegisterPage